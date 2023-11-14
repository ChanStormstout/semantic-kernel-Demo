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
chat_function = kernel.create_semantic_function(sk_prompt, "ChatBot", max_tokens=2000, temperature=0.7, top_p=0.5)
context = kernel.create_new_context()
context["history"] = ""
   

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

async def generate(prompts):
    await chat(prompts)


# 使用 asyncio.run 运行 main 协程
# asyncio.run(generate())

# 先成功调用这个函数
# 成功调用a, 调用b, 调用C
# 假设有了dependency
