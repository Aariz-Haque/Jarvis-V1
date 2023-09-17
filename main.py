# from IO.listen import listen
import os
from IO.speak import speak
os.system('cls')
from Intelligence.conversation import getResponse
while True:
    q=input("Enter query: ")
    r=getResponse(q)
    print(r)
    speak(r)
    