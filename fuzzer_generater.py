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

# initialize the context
context = kernel.create_new_context()
context["history"] = ""

# Step 1: accept the code snippet and analyze.
prompt1 = """{{$input}}
    Analyze the code snippet that I gave to you.
"""
step1_func = kernel.create_semantic_function(prompt1, max_tokens=2000, temperature=0.2, top_p=0.5)
code_snippet1 = """
// Copyright 2016 Google Inc. All Rights Reserved.
// Licensed under the Apache License, Version 2.0 (the "License");

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

bool VulnerableFunction2(const uint8_t* data, size_t size, bool verify_hash) {
  if (size < sizeof(kMagicHeader))
    return false;

  std::string header(reinterpret_cast<const char*>(data), sizeof(kMagicHeader));

  std::array<uint8_t, kMaxBodyLength> body;

  if (strcmp(kMagicHeader, header.c_str()))
    return false;

  auto target_hash = data[--size];

  if (size > kMaxPacketLen)
    return false;

  if (!verify_hash)
    return true;

  std::copy(data, data + size, body.data());
  auto real_hash = DummyHash(body);
  return real_hash == target_hash;
}


constexpr std::size_t kZn2016VerifyHashFlag = 0x0001000;

bool VulnerableFunction3(const uint8_t* data, size_t size, std::size_t flags) {
  bool verify_hash = flags & kZn2016VerifyHashFlag;
  return VulnerableFunction2(data, size, verify_hash);
}


#endif // LESSONS_04_VULNERABLE_FUNCTIONS_H_
}

"""
output1 = step1_func(code_snippet1)
print(f"Output: {output1}\n")

# insert a step: query more precisely, focus on a specific function.
prompt_i = """
  {{$history}}
  User: {{$user_input}}
  ChatBot:
  Analyze the code of the function `VulnerableFunction1`.
  What is the type of its input parameter? What is the type of the output result?
"""
step_i_func = kernel.create_semantic_function(prompt_i, max_tokens=2000, temperature=0.2, top_p=0.5)
output_i = step_i_func(prompt_i)
print(f"\033[32mOutput_insert: {output_i}\n\033[0m")

# Step 2: tell the llm about the input/outputs' types.
prompt2 = """ 
  Now generate a function `LLVMFuzzerTestOneInput` that accepts `const uint8_t*` as the input parameter's type,
  and returns a result of type `size_t` in C language.This function should be written based on the `VulnerableFunction1` function.
"""
step2_func = kernel.create_semantic_function(prompt2, max_tokens=2000, temperature=0.2, top_p=0.5)
code_snippet2 = """
// Copyright 2016 Google Inc. All Rights Reserved.
// Licensed under the Apache License, Version 2.0 (the "License");

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

bool VulnerableFunction2(const uint8_t* data, size_t size, bool verify_hash) {
  if (size < sizeof(kMagicHeader))
    return false;

  std::string header(reinterpret_cast<const char*>(data), sizeof(kMagicHeader));

  std::array<uint8_t, kMaxBodyLength> body;

  if (strcmp(kMagicHeader, header.c_str()))
    return false;

  auto target_hash = data[--size];

  if (size > kMaxPacketLen)
    return false;

  if (!verify_hash)
    return true;

  std::copy(data, data + size, body.data());
  auto real_hash = DummyHash(body);
  return real_hash == target_hash;
}


constexpr std::size_t kZn2016VerifyHashFlag = 0x0001000;

bool VulnerableFunction3(const uint8_t* data, size_t size, std::size_t flags) {
  bool verify_hash = flags & kZn2016VerifyHashFlag;
  return VulnerableFunction2(data, size, verify_hash);
}


#endif // LESSONS_04_VULNERABLE_FUNCTIONS_H_

"""

output2 = step2_func(code_snippet2)
print(f"Output2 : {output2}\n")