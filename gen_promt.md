You are ChatGPT, a large language model trained by OpenAI. And you are the greatest one in Fuzzing and program anaylysis. Generate a fuzz driver function called LLVMFuzzerTestOneInput, 
which accpets a `const uint8_t*` (called data) and a `size_t` parameter as the inputs,  
and be able to invoke the following function: ``. And it should have an extern "C" prefix. 

You can write some class or function to invoke the target function if neccessary. The function you generate must use the input 'data' and 'size' parameters. 
Please assure that the Generated code includes the neccessary head files. And make sure that your generated code begins and ends with a new line containing "==========" as the content.

<!-- clang++ -g test_fuzzer.cc -O2  /home/victor/workspace/fuzzing_target_repo/easywsclient/easywsclient.cpp -I/home/victor/workspace/fuzzing_target_repo/easywsclient/ -o fuzz_executable $LIB_FUZZING_ENGINE -->
