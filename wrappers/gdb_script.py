import gdb

gdb.execute("file /home/victor/workspace/semantic-kernel-Demo/fuzz_executable")
gdb.execute("run")

# capture backtrace
bt = gdb.execute("bt", to_string=True)

# save/process backtrace
with open("backtrace.log", "w") as file:
    file.write(bt)