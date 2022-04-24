import subprocess
import platform
import psutil
import time
import os

def get_wm():
    output = subprocess.run(["wmctrl", "-m"], text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if output.stderr:
        return output.stderr
    else:
        split = output.stdout.split("\n")
        res = split[0].split("Name: ")[1]

        return res

def get_sh():
    return psutil.Process(os.getpid()).parent().name()

def get_system():
    os = platform.system()
    version = platform.release()
    
    new_v = ""
    version = version.replace("5.17.3-", "").replace("1-1", "")
    for x, char in enumerate(version):
        if x == 0:
            char = char.upper()
            new_v += char
        else:
            new_v += char
    return new_v + "-" + os

def get_colors():
    return "\033[91m\uf05b \033[96m\uf05b \033[93m\uf05b \033[94m\uf05b \033[95m\uf05b \033[90m\uf05b \033[0m"

def get_time():
    return time.strftime("%H:%M")

def main():
    try:
        wm = get_wm()
        sh = get_sh()
        if os.name == "nt":
            os.system("mode 12 12")
        os.system("clear")
        print("  " + get_system())
        print(" ------------")
        print(" WM    | " + wm)
        print(" Shell | " + sh + "\n")
        print(" " + get_colors())
        print("")
        print("  | " + get_time() + " | ")
    except KeyboardInterrupt:
        exit(0)

while True:
    main()
