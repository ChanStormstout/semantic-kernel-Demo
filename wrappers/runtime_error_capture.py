import subprocess

def capture_bt():
    subprocess.run(["gdb", "-x", "/home/victor/workspace/semantic-kernel-Demo/wrappers/gdb_script.py"])

    # 读取并处理 backtrace 信息
    with open("backtrace.log", "r") as file:
        backtrace_info = file.read()
        print(backtrace_info)
    
    return backtrace_info

# print(capture_bt())