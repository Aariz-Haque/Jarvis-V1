# from IO.listen import listen
import os
from IO.speak import speak
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from Intelligence.conversation import getResponse
from time import sleep
from Security.security import validateUser
from Functions.functionsforchatbot import *
os.system('cls')
console=Console()


def initializeJarvis():
    directory_path="Prompts"
    for filename in track(os.listdir(directory_path),description="Initializing JARVIS..."):
        
        if filename.startswith("prompt_") and filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
                content = file.read()
        getResponse(content)
if(validateUser()):

    
    for _ in track(range(100),description="[bold][green]Loading...[/][/]"):
        sleep(0.001)
    initializeJarvis()
    text="""# Welcome to J.A.R.V.I.S """
    md=Markdown(text)
    console.print(md)

    

    while True:
        q=input("Enter query: ")
        r=getResponse(q)
        tokenedList=r.split("\n")
        
        matched_strings=[]
        index_to_remove=[]
        for i, item in enumerate(tokenedList):
            if isinstance(item, str) and item.startswith("func_"):
                matched_strings.append(item)
                index_to_remove.append(i)
        for i in reversed(index_to_remove):
            tokenedList.pop(i)
        for i in matched_strings:

            # print(i)
            exec(i)
        
        if not matched_strings:
            print(r)
            speak(r)
        
else:
    text="""# Access Denied"""
    md=Markdown(text)
    console.print(md)
    speak("Access Denied")