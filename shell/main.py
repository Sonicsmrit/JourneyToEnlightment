import sys
import os
import shutil
import subprocess
import shlex
import readline



def main():

    # TODO: Uncomment the code below to pass the first stage

    option = ["exit ", "echo "]
    def complete(text, status):
        to_complete = []
        for x in option:
            if x.startswith(text):
                to_complete.append(x)
        for directory in os.environ.get("PATH", "").split(os.pathsep):
            if not os.path.isdir(directory):
                continue
            try:
                for name in os.listdir(directory):
                    full = os.path.join(directory, name)
                    if name.startswith(text) and os.access(full, os.X_OK) and not os.path.isdir(full):
                        to_complete.append(name)
            except PermissionError:
                pass
    

        if status < len(to_complete):
            if len(to_complete) == 1:
                return to_complete[status] + " "
            else:
                return to_complete[status]
        else:
            return None

    

    readline.set_completer_delims("")
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)
    
    

    while True:
        
        sys.stdout.write("$ ")
        command = input()
        
        

        if ">" in command or "1>" in command:
            os.system(command)
            continue
        
        elif command == "exit":
            break
        
        elif command.startswith("echo"):
            if '"' in command[4:]:
                change = shlex.split(command[4:])
                change =" ".join(change).strip()
                print(change)
            else:
                echo_value = shlex.split(command[4:])
                print(" ".join(echo_value))

        elif command.startswith("cat"):
            avgs = ["cat"] + shlex.split(command[4:])
            subprocess.run(avgs)

        elif command.startswith("'") or command.startswith('"'):
            echo_value = shlex.split(command)
            subprocess.run(echo_value)


        
        elif command.strip() == "pwd":
            path = os.getcwd()
            print(path)
        
        elif command[0:2] == "cd":
            if command.strip().split()[1] == "~":
                home = os.path.expanduser("~")
                os.chdir(home)


            else:   
                new_dic = command[2:].strip()
                try:
                    os.chdir(new_dic)
                except:
                    print(f"cd:{command[2:]}: No such file or directory")
    
        elif command[0:4] == "type":
            if command[4:].strip() == "echo":
                print("echo is a shell builtin")
            elif command[4:].strip() == "exit":
                print("exit is a shell builtin")
            elif command[4:].strip() == "type":
                print("type is a shell builtin")
            elif command[4:].strip() == "pwd":
                print("pwd is a shell builtin")
            elif command[4:].strip() == "cd":
                print("cd is a shell builtin")
            
            elif path := shutil.which(command[4:].strip()):
                print(f"{command[4:].strip()} is {path}")  
                    
            else:
                print(f"{command[4:].strip()}: not found")
        

        elif execution := shutil.which(shlex.split(command)[0]):
            exc = shlex.split(command)
            subprocess.run(exc)

        else:
            print(f"{command}: not found")



        

        pass
        


if __name__ == "__main__":
    main()
