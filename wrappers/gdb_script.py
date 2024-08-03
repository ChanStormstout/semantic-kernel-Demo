import gdb

# 设置要调试的程序和参数
gdb.execute("file /home/victor/workspace/semantic-kernel-Demo/fuzz_executable")

# 运行程序
gdb.execute("run")

# 捕获 backtrace
bt = gdb.execute("bt", to_string=True)

# 捕获其他潜在有用的信息
registers = gdb.execute("info registers", to_string=True)
memory_info = gdb.execute("x/10gx $rsp", to_string=True)

# 组合所有信息
full_output = "Backtrace:\n" + bt + "\nRegisters:\n" + registers + "\nMemory Info:\n" + memory_info

# 保存信息到文件
with open("debug_info.log", "w") as file:
    file.write(full_output)
