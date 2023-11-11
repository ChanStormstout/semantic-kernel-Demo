import asyncio
from ContinuousChatRobot import generate
from c_fuzzer_wrapper import CFuzzerWrapper

# Prompts design
source_code_prompt = "Please analyze the following code: \n"
use_case_prompt = "Please accept cases that call the target function within the same repository. \n"
document_prompt = "Please receive the following related document: \n"
generate_prompt = """Generate a function called LLVMFuzzerTestOneInput, which accpets a `const uint8_t*` (called data) and a `size_t` parameter as the inputs, 
                    and be able to invoke the function """
generate_prompt_suffix =  "Please note that you can only give me the code without any expalain."
async def call_LLM(prompts):
    await generate(prompts)

async def main():
    # Create a CFuzzerWrapper instance and pass the knowledge information
    c_fuzzer = CFuzzerWrapper(language_type='C/C++')
    c_fuzzer.set_target_function_from_input()
    c_fuzzer.collect_knowledge()

    formatted_source_code = source_code_prompt + c_fuzzer.knowledge_receiver.source_code
    formatted_use_case = use_case_prompt + c_fuzzer.knowledge_receiver.use_case
    formatted_document = document_prompt + c_fuzzer.knowledge_receiver.document_content
    formatted_generate_prompt = generate_prompt + c_fuzzer.target_function + generate_prompt_suffix

    # test-code
    # print(c_fuzzer.knowledge_receiver.document_content)
    await(call_LLM(formatted_source_code))
    await(call_LLM(formatted_use_case))
    await(call_LLM(formatted_document))
    await(call_LLM(formatted_generate_prompt))
    await(call_LLM("Do you need more details?"))
    # Additional information / Extra loop (Need to have the limitation of the round number?)
    loop_counter = 0  # 初始化计数器
    while loop_counter < 5:  # 循环最多执行5次
        user_input = input("Input right here: ")
        if user_input.lower() == 's':  # 如果用户输入's'，则退出循环
            break
        await call_LLM(user_input)

        loop_counter += 1  # 每次循环后增加计数器

if __name__ == "__main__":
    asyncio.run(main())