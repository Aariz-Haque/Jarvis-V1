from Intelligence.conversation import getResponse
from IO.listen import listen
from IO.speak import speak
while True:
    q=listen()
    r=getResponse(q)
    print(r)
    speak(r)
    