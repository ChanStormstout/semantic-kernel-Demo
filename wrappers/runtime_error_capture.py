import subprocess

# def capture_bt():
#     # subprocess.run(["gdb", "-x", "/home/victor/workspace/semantic-kernel-Demo/wrappers/gdb_script.py"])
#     subprocess.run("gdb -ex "run" -ex "quit" --args /home/victor/workspace/semantic-kernel-Demo/fuzz_executable &> asan_report.log")
#     # 读取并处理 backtrace 信息
#     with open("backtrace.log", "r") as file:
#         backtrace_info = file.read()
#         print(backtrace_info)
    
#     return backtrace_info

def run_gdb_and_capture_output():
    command = 'gdb -ex "run" -ex "quit" --args /home/victor/workspace/semantic-kernel-Demo/fuzz_executable'
    with open('asan_report.log', 'w') as file:
        subprocess.run(command, shell=True, stdout=file, stderr=subprocess.STDOUT)

    with open("asan_report.log", "r") as file:
        debug_info = file.read()
        return debug_info