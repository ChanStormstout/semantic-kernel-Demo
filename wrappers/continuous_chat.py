import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

kernel = sk.Kernel()
# Configure AI service used by the kernel
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-4", api_key, org_id))

sk_prompt = """
ChatBot can have a conversation with you about code generation and analysis. And ChatBot is an expert in Fuzzing and program anaylysis.
It can give explicit instructions or say 'I need more information/details' if it does not have an answer.

{{$history}}
User: {{$user_input}}
ChatBot: """

gen_prompt = """
{{$history}}
Generate a fuzz driver function called LLVMFuzzerTestOneInput, 
which accpets a `const uint8_t*` (called data) and a `size_t` parameter as the inputs,  
and be able to invoke the function `{{$targetFunction}}`. And it should have an extern "C" prefix. 

Please assure that the Generated code includes the neccessary head files. And make sure that your generated code begins and ends with a new line containing "==========" as the content. 
Generated_code: 
"""

compile_modify_prompt = """
Compilation correction history information:
{{$compilation_history}}

The following is a source code for fuzzing using libFuzzer, with target function as {{$targetFunction}}:
{{$generated_code}}
The following error occurred during the compilation process : {{$compilation_error}}
Can you modify this function and return the correct code to me? Please make sure to keep the original code's header files and macro definitions, and return the complete code. Please be sure to include the entire code without any omissions!
And the target function's source code is as follow :
{{$target_source_code}}

Assure that the Generated code includes the neccessary head files. And make sure that your generated code begins and ends with a new line containing "==========" as the content. 
"""

runtime_erro_modify_prompt = """
You're an expert in Fuzzing and program anaylysis.
You can give explicit instructions or say 'I need more information/details' if you do not have an answer.

The following is a source code for fuzzing using libFuzzer, with target function as {{$targetFunction}}:
{{$generated_code}}
Runtime error correction history information:
{{$runtime_modify_history}}

During the process of program execution, the following error is encountered:
{{$runtime_error}}
Can you modify this function and return the correct code to me? Please make sure to keep the original code's header files and macro definitions, and return the complete code. Please be sure to include the entire code without any omissions!
And the target function's source code is as follow :
{{$target_source_code}}
Assure that the Generated code includes the neccessary head files. And make sure that your generated code begins and ends with a new line containing "==========" as the content. 
"""

chat_function = kernel.create_semantic_function(sk_prompt, "ChatBot", max_tokens=2000, temperature=0.7, top_p=0.5)
generate_function = kernel.create_semantic_function(gen_prompt, "GenBot", max_tokens=2000, temperature=0.7, top_p=0.5)
compile_modify_function = kernel.create_semantic_function(compile_modify_prompt, "CompilationModify", max_tokens=2000, temperature=0.7, top_p=0.5)
runtime_modify_function = kernel.create_semantic_function(runtime_erro_modify_prompt, "RuntimeModify", max_tokens=2000, temperature=0.7, top_p=0.5)

context = kernel.create_new_context()
context["history"] = ""
context["target_source_code"] = ""
context["compilation_history"] = ""
context["generated_code"] = ""
context["runtime_modify_history"] = ""

# define async function
async def chat(input_text: str) -> None:
    # initialize the context
    
    # Save new message in the context variables
    print(f"\033[93mUser: {input_text}\033[0m")
    context["user_input"] = input_text

    # Process the user message and get an answer
    answer = await chat_function.invoke_async(context=context)

    # Show the response
    print(f"\033[32mChatBot: {answer}\n\033[0m")

    # Append the new interaction to the chat history
    context["history"] += f"\nUser: {input_text}\nChatBot: {answer}\n"

def process_string(input_string):
    # 找到第一个 '#' 的位置
    start_index = input_string.find('#')
    # 找到最后一个 '==========' 的位置
    end_index = input_string.rfind('==========')

    # 如果找到了 '#' 和 '=========='
    if start_index != -1 and end_index != -1:
        # 提取这两个索引之间的内容
        result = input_string[start_index:end_index]
    else:
        result = input_string

    return result

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

async def generate(target_func: str):
    print(f"\033[93mTarget_function: {target_func}\033[0m")
    context["target_function"] = target_func
    generated_content = await generate_function.invoke_async(context=context)
    print(f"\033[32mGenBot: {generated_content}\n\033[0m")
    context["history"] += f"\ntarget_function: {target_func}\nGenBot: {generated_content}\n"
    generated_code = generated_content.result
    save_code = process_string(generated_code)
    context["generated_code"] = save_code
    save_to_file(save_code, 'test_fuzzer.cc')
    return save_code

async def compile_modify(target_source_code: str, compilation_error_message: str):
    context["target_source_code"] = target_source_code
    context["compilation_error"] = compilation_error_message
    new_version_content = await compile_modify_function.invoke_async(context=context)
    new_version_code = new_version_content.result
    save_code = process_string(new_version_code)
    context["generated_code"] = save_code
    save_to_file(save_code, 'test_fuzzer.cc')

async def runtime_erro_modify(target_source_code: str, runtime_error_message: str):
    context["target_source_code"] = target_source_code
    context["runtime_error"] = runtime_error_message
    new_version_content = await runtime_modify_function.invoke_async(context=context)
    new_version_code = new_version_content.result
    save_code = process_string(new_version_code)
    context["generated_code"] = save_code
    save_to_file(save_code, 'test_fuzzer.cc')

# 使用 asyncio.run 运行 main 协程
# asyncio.run(generate("printf"))

# 先成功调用这个函数
# 成功调用a, 调用b, 调用C
# 假设有了dependency
