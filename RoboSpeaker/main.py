# Will only run on macOS
# import os
#
# if __name__ == "__main__":
#     print("Welcome to RoboSpeaker 1.1. Created By Aarish")
#     while True:
#         x = input("Enter what you want to speak: ")
#         if x == "q":
#             os.system("say 'Bye bye Friend. Nice to meet you'")
#             break
#         command = f"say {x}"
#         os.system(command)

# Will only run on Windows

import win32com.client # pip install pywin32

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created By Aarish")
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "q":
            speaker.Speak("Bye bye Friend. Nice to meet you")
            break
        speaker.Speak(x)
