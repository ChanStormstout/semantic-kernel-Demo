import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

kernel = sk.Kernel()
# Configure AI service used by the kernel
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

sk_prompt = """
ChatBot can have a conversation with you about any topic.
It can give explicit instructions or say 'I don't know' if it does not have an answer.

{{$history}}
User: {{$user_input}}
ChatBot: """

gen_prompt = """
Generate a fuzz driver function called LLVMFuzzerTestOneInput, 
which accpets a `const uint8_t*` (called data) and a `size_t` parameter as the inputs,  
and be able to invoke the function {{$targetFunction}}

Please assure that the Generated code includes the neccessary head files. And make sure that your generated code begins and ends with a new line containing "==========" as the content. 
{{$history}}
Generated_code: """

chat_function = kernel.create_semantic_function(sk_prompt, "ChatBot", max_tokens=2000, temperature=0.7, top_p=0.5)
generate_function = kernel.create_semantic_function(gen_prompt, "GenBot", max_tokens=2000, temperature=0.7, top_p=0.5)
# initialize the context
context = kernel.create_new_context()
context["history"] = ""


# define async function
async def chat(input_text: str) -> None:
    # Save new message in the context variables
    print(f"\033[93mUser: {input_text}\033[0m")
    context["user_input"] = input_text

    # Process the user message and get an answer
    answer = await chat_function.invoke_async(context=context)

    # Show the response
    print(f"\033[32mChatBot: {answer}\n\033[0m")

    # Append the new interaction to the chat history
    context["history"] += f"\nUser: {input_text}\nChatBot: {answer}\n"

async def generate(target_func: str):
    print(f"\033[93mTarget_function: {target_func}\033[0m")
    context["target_function"] = target_func
    generated_code = await generate_function.invoke_async(context=context)
    print(f"\033[32mGenBot: \n{generated_code}\n\033[0m")
    context["history"] += f"\ntarget_function: {target_func}\nGenBot: {generated_code}\n"

async def main():
    # user_input1 = input("")
    # user_input2 = input("input2: ")
    # user_input3 = input("input3: ")
    # user_input4 = input("input4: ")
    await generate("printf")
    #await chat(user_input2)
    #await chat(user_input3)
    #await chat(user_input4)

# 使用 asyncio.run 运行 main 协程
asyncio.run(main())

# 先成功调用这个函数
# 成功调用a, 调用b, 调用C
# 假设有了dependency
