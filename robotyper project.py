import os
if __name__ == '__main__':
    print("welcome to RoboSpeaker by Vivek")
    while True:
        x= input("Enter what you want me to speak :")
        if x == "q":
            os.system("echo bye bye friend")
            break
        command =f"echo {x}"
        os.system(command)