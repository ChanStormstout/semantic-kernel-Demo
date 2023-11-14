import subprocess

def compile_and_link(source_file, object_files, output_executable):
    compile_command = ["clang", "-g", "-o", output_executable, source_file] + object_files
    try:
        subprocess.run(compile_command, check=True)
    except subprocess.CalledProcessError as e:
        with open("compile_errors.log", "w") as log_file:
            log_file.write(str(e))

# 调用函数
compile_and_link("/home/victor/workspace/semantic-kernel-Demo/lessons/04/hello.c", [], "fuzz_executable")
