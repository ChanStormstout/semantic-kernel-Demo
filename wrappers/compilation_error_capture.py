import subprocess
import json
import os

YELLOW = "\033[33m"
RESET = "\033[0m"  # 重置颜色

def extract_include_dirs(file_path, target_file):
    """
    Extracts and returns a list of directories specified by the `-I` option for a given target file
    in the compile_commands.json file at the given file path.

    :param file_path: Path to the compile_commands.json file.
    :param target_file: Name of the target file (e.g., "ssl_lib.c").
    :return: A list of directories specified by the `-I` option for the target file.
    """
    include_dirs = []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for command in data:
                # Check if the command is for the target file
                if command.get("file", "").endswith(target_file):
                    directory = command.get("directory", "")
                    args = command.get("arguments", [])
                    for arg in args:
                        if arg.startswith('-I'):
                            include_path = arg[2:]
                            # Resolve the absolute path if the include path is relative
                            full_path = os.path.normpath(os.path.join(directory, include_path))
                            include_dirs.append(full_path)
                    break
    except Exception as e:
        print(f"Error reading file: {e}")

    return include_dirs

def find_static_libs(directory):
    """
    Recursively searches for .a files in a given directory and returns their absolute paths.

    :param directory: The directory to search in.
    :return: A list of absolute paths to .a files.
    """
    static_libs = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".a"):
                static_libs.append(os.path.join(root, file))
    return static_libs

def get_libraries_from_user(input):
    libraries = input.split()  # 使用空格分隔路径
    return libraries

def compile_and_link(source_file, include_dirs, output_executable, libraries):
    # 构建编译命令
    compile_command = ["clang++", "-g", source_file, "-O2", "-fno-omit-frame-pointer",
                       "-fsanitize=address,fuzzer", "-fsanitize-coverage=trace-cmp,trace-gep,trace-div"]

    # 添加 -I 参数
    for dir in include_dirs:
        compile_command.append("-I" + dir)

    # 添加用户指定的库（静态库或动态库）
    compile_command += libraries

    # 添加输出可执行文件的参数
    compile_command.append("-o")
    compile_command.append(output_executable)

    # 打印编译命令
    print(YELLOW + "Compiling with command:", ' '.join(compile_command) + RESET)

    # 执行编译命令
    try:
        subprocess.run(compile_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        error_message = e.stderr  # 捕获详细的错误信息
        print("Compile ERROR:")
        print(error_message)
        with open("compile_errors.log", "w") as error_file:
            error_file.write(error_message)
        return error_message  # 可以选择返回错误信息，或者写入文件等


# directory = '/home/victor/fuzzing/libfuzzer-workshop/lessons/05'  # Replace with the actual directory path
# file_path = '/home/victor/fuzzing/libfuzzer-workshop/lessons/05/openssl1.0.1f/compile_commands.json'
# target_file = 'ssl_lib.c'
# include_dirs = extract_include_dirs(file_path, target_file)
# static_libs_dir = '/home/victor/fuzzing/libfuzzer-workshop/lessons/05'

# 调用函数
# libraries = ["/home/victor/fuzzing/libfuzzer-workshop/lessons/05/openssl1.0.1f/libssl.a", "/home/victor/fuzzing/libfuzzer-workshop/lessons/05/openssl1.0.1f/libcrypto.a"]
# libraries = get_libraries_from_user()
# source_file = "/home/victor/fuzzing/libfuzzer-workshop/lessons/05/openssl_fuzzer.cc"
# output_executable = "fuzz_executable"
# compile_and_link(source_file, include_dirs, output_executable, libraries)