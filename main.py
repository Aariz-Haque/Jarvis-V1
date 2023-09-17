# from IO.listen import listen
import os
from IO.speak import speak
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
from Intelligence.conversation import getResponse
from time import sleep
from Security.security import validateUser

os.system('cls')
console=Console()
if(validateUser()):

    
    for _ in track(range(100),description="[bold][green]Loading...[/][/]"):
        sleep(0.001)
    text="""# Welcome to J.A.R.V.I.S """
    md=Markdown(text)
    console.print(md)


    while True:
        q=input("Enter query: ")
        r=getResponse(q)
        print(r)
        speak(r)
else:
    text="""# Access Denied"""
    md=Markdown(text)
    console.print(md)
    speak("Access Denied")