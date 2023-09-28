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
# initialize the context
context = kernel.create_new_context()
context["history"] = ""

# define the texts
text_1 = """
Given the following code:
#ifndef LESSONS_04_VULNERABLE_FUNCTIONS_H_
#define LESSONS_04_VULNERABLE_FUNCTIONS_H_

#include <stdint.h>
#include <stddef.h>
#include <cstring>

#include <array>
#include <string>
#include <vector>


bool VulnerableFunction1(const uint8_t* data, size_t size) {
  bool result = false;
  if (size >= 3) {
    result = data[0] == 'F' &&
             data[1] == 'U' &&
             data[2] == 'Z' &&
             data[3] == 'Z';
  }

  return result;
}


template<class T>
typename T::value_type DummyHash(const T& buffer) {
  typename T::value_type hash = 0;
  for (auto value : buffer)
    hash ^= value;

  return hash;
}

constexpr auto kMagicHeader = "ZN_2016";
constexpr std::size_t kMaxPacketLen = 1024;
constexpr std::size_t kMaxBodyLength = 1024 - sizeof(kMagicHeader);



constexpr std::size_t kZn2016VerifyHashFlag = 0x0001000;

bool VulnerableFunction3(const uint8_t* data, size_t size, std::size_t flags) {
  bool verify_hash = flags & kZn2016VerifyHashFlag;
  return VulnerableFunction3(data, size, verify_hash);
}


#endif // LESSONS_04_VULNERABLE_FUNCTIONS_H_
}

Your task is to analyze the provided code snippet. Please provide a clear and concise response that explains the purpose of the code, and its key components.

Please note that your analysis should be flexible enough to accommodate different types of code snippets, such as functions, classes, or algorithms. You should focus on providing a thorough and accurate assessment of the code, highlighting both its strengths and weaknesses.
"""

text_2 = """
Please analyze the VulnerableFunction1 function in the provided code. Your task is to determine the type of input parameters it accepts and the type of output it produces. Please provide a clear and concise response that accurately describes the input parameter type(s) and the output type of the VulnerableFunction1 function.

Please note that your response should be based on a careful analysis of the code provided.
"""

text_3 = """
Please create an LLVMFuzzerTestOneInput function in C language that is based on the VulnerableFunction1 function. The function should have a single input parameter of type const uint8_t* and should return a variable named result of type size_t.

Your LLVMFuzzerTestOneInput function should take the input parameter and perform the necessary operations to generate a result value. The specific implementation details and logic of the function should be based on the behavior of the VulnerableFunction1 function.

Please ensure that your LLVMFuzzerTestOneInput function adheres to the requirements stated above and follows best practices for writing secure and efficient code.
"""
text_4 = """
Hello AI Assistant,

I need your help to generate a fuzz driver function for the code I provided. Specifically, I want to create a fuzz driver function for the `VulnerableFunction3` function. The code for the fuzz driver should be written in C and should have the following structure:

```
#include <stdint.h>
#include <stddef.h>

#include "vulnerable_functions.h"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
  VulnerableFunction1(data, size);
  return 0;
}
```

Now, I also need you to infer the fuzz driver function for the `VulnerableFunction3` function. Please note that the `VulnerableFunction3` function has additional input parameters that accept a size_t variable. Take this into consideration when creating the fuzz driver function.
"""
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

async def main():
    await chat(text_1)
    await chat(text_2)
    await chat(text_3)
    await chat(text_4)

# 使用 asyncio.run 运行 main 协程
asyncio.run(main())

# 先成功调用这个函数
# 成功调用a, 调用b, 调用C
# 假设有了dependency
