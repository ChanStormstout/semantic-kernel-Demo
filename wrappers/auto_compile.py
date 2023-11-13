import subprocess
import json

def compile_project(compile_commands_file):
    with open(compile_commands_file, 'r') as file:
        commands = json.load(file)

    for command in commands:
        # 获取编译命令和目录
        compile_command = command['arguments']
        working_directory = command['directory']

        # 执行编译命令
        try:
            subprocess.run(compile_command, cwd=working_directory, check=True)
            print(f"Compiled: {command['file']}")
        except subprocess.CalledProcessError as e:
            print(f"Error compiling {command['file']}: {e}")
