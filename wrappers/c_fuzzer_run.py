import asyncio
from continuous_chat import generate,chat
from c_fuzzer_wrapper import CFuzzerWrapper
from auto_compile import compile_project
from compilation_error_capture import compile_and_link
from runtime_error_capture import capture_bt

# Prompts design
source_code_prompt = "Please analyze the following code: "
use_case_prompt = "Please accept cases that call the target function within the same repository. \n"
document_prompt = "Please accept the following related document: \n"
generate_prompt = """Generate a function called LLVMFuzzerTestOneInput, which accpets a `const uint8_t*` (called data) and a `size_t` parameter as the inputs,  and be able to invoke the function `"""
generate_prompt_suffix =  "`. Please note that you can just only give me the code without any other words."
async def call_LLM(prompts):
    await chat(prompts)

async def main():
    # Create a CFuzzerWrapper instance and pass the knowledge information
    c_fuzzer = CFuzzerWrapper(language_type='C/C++')
    target_func_name = input("Please enter the target function: ")
    c_fuzzer.target_function = target_func_name
    c_fuzzer.collect_knowledge()

    formatted_source_code = source_code_prompt + c_fuzzer.knowledge_receiver.source_code
    formatted_use_case = use_case_prompt + c_fuzzer.knowledge_receiver.use_case
    formatted_document = document_prompt + c_fuzzer.knowledge_receiver.document_content
    formatted_generate_prompt = generate_prompt + c_fuzzer.target_function + generate_prompt_suffix

    if(c_fuzzer.knowledge_receiver.source_code != ""):
        await(call_LLM(formatted_source_code))
    if(c_fuzzer.knowledge_receiver.use_case != ""):
        await(call_LLM(formatted_use_case))
    if(c_fuzzer.knowledge_receiver.document_content != ""):
        await(call_LLM(formatted_document))
    await(call_LLM(formatted_generate_prompt))
    
    print("Do you want to input more details about the target function?")
    # Additional information / Extra loop (Need to have the limitation of the round number?)
    loop_counter = 0  # 初始化计数器
    while loop_counter < 5:  # 循环最多执行5次
        user_input = input("Input right here: ")
        if user_input.lower() == 's':  # 如果用户输入's'，则退出循环
            break
        await call_LLM(user_input)

        loop_counter += 1  # 每次循环后增加计数器


    # auto-compile module
    # compile_commands_file = '/home/victor/workspace/fuzzing_target_repo/gpac/compile_commands.json'  # 设置文件路径
    # compile_project(compile_commands_file)

    # error capture module
    # 1. compilation error capture
    # compile_and_link("/home/victor/workspace/semantic-kernel-Demo/lessons/04/hello.c", [], "fuzz_executable")

    # 2. runtime error capture
    # capture_bt()

if __name__ == "__main__":
    asyncio.run(main())