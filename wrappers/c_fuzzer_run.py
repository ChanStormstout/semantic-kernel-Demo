import asyncio
from ContinuousChatRobot import generate
from c_fuzzer_wrapper import CFuzzerWrapper

async def call_LLM(prompts):
    await generate(prompts)

async def main():
    # 下面创建一个CFuzzerWrapper实例并传递知识
    c_fuzzer = CFuzzerWrapper(language_type='C/C++')
    c_fuzzer.collect_knowledge()

    print(c_fuzzer.knowledge_receiver.document_content)
    await(call_LLM(c_fuzzer.knowledge_receiver.document_content))
    

if __name__ == "__main__":
    asyncio.run(main())