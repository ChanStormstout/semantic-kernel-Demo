import asyncio
import json
import subprocess
from continuous_chat import chat, generate, compile_modify, runtime_erro_modify
from c_fuzzer_wrapper import CFuzzerWrapper
from compilation_error_capture import compile_and_link, get_libraries_from_user, extract_include_dirs
from runtime_error_capture import run_gdb_and_capture_output
from extract_info import read_file

with open('function_information/config.json', 'r') as file:
    config = json.load(file)

# Prompts design
source_code_prompt = "Analyze the following code: "
use_case_prompt = "Please accept cases that invoke the target function within the same repository: \n"
document_prompt = "Please accept the following related document: \n"

source_code_file = config["source_code_file"]
dependency_prompt = "The source code of the target function is in the `" + source_code_file + "` file, and its dependencies are as follows: "

async def call_LLM(prompts):
    await chat(prompts)

async def main():
    # Create a CFuzzerWrapper instance and pass the knowledge information
    c_fuzzer = CFuzzerWrapper(language_type='C/C++')
    c_fuzzer.target_function = config["target_function"]
    c_fuzzer.collect_knowledge()

    formatted_source_code = source_code_prompt + c_fuzzer.knowledge_receiver.source_code
    formatted_use_case = use_case_prompt + c_fuzzer.knowledge_receiver.use_case
    formatted_document = document_prompt + c_fuzzer.knowledge_receiver.document_content
    formatted_dependency = dependency_prompt + '\n'.join(c_fuzzer.knowledge_receiver.dependencies)
    print(formatted_dependency)
    if(c_fuzzer.knowledge_receiver.source_code != ""):
        await(chat(formatted_source_code))
    if(c_fuzzer.knowledge_receiver.document_content != ""):
        await(chat(formatted_document))
    if(c_fuzzer.knowledge_receiver.use_case != ""):
        await(chat(formatted_use_case))


    await(call_LLM(formatted_dependency))
    await(generate(c_fuzzer.target_function))
    
    # print("Do you want to input more details about the target function?")
    # Additional information / Extra loop (Need to have the limitation of the round number?)
    # loop_counter = 0  # 初始化计数器
    # while loop_counter < 5:  # 循环最多执行5次
    #     user_input = input("Input right here: ")
    #     if user_input.lower() == 'n':  # 如果用户输入'n'，则退出循环
    #         break
    #     await call_LLM(user_input)
    #     loop_counter += 1  # 每次循环后增加计数器


    # auto-compile module
    file_path = config["compile_json_path"]
    target_file = config["source_code_file"]
    include_dirs = extract_include_dirs(file_path, target_file)
    libraries = get_libraries_from_user(config["lib_path"])
    compile_error = compile_and_link("test_fuzzer.cc", include_dirs, "fuzz_executable", libraries)
    round = 1
    while compile_error is not None and round <= 6: 
        print(f"Now is the {round} round.")
        code_content = read_file("test_fuzzer.cc")
        await compile_modify(code_content, compile_error)
        compile_error = compile_and_link("test_fuzzer.cc", include_dirs, "fuzz_executable", libraries)
        round += 1

    # error capture module
    # 1. compilation error capture
    # compile_and_link("/home/victor/workspace/semantic-kernel-Demo/lessons/04/hello.c", [], "fuzz_executable")

    # 2. runtime error capture
    try:
        result = subprocess.run(["./fuzz_executable"], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Program output:", result.stdout)
    
    except subprocess.CalledProcessError as e:
    # Catch the exception if the program exits with a non-zero exit code
        print("Program encountered an error, Exit Code:", e.returncode)
        print("Error Output:", e.stderr)
        backtrace_info = run_gdb_and_capture_output()
        code_content = read_file("test_fuzzer.cc")
        await runtime_erro_modify(code_content, backtrace_info)
        # while backtrace_info is not None and compile_error is not None and round <= 6: 
        #     code_content = read_file("test_fuzzer.cc")
        #     await runtime_erro_modify(code_content, backtrace_info)
            # 这里需要一个新的对于compile_error修改的循环。 考虑把这个compile_error的修改封装成函数
    except Exception as e:
        # Catch all other exceptions
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    asyncio.run(main())