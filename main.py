from Intelligence.conversation import getResponse
while True:
    q=input("Enter query")
    r=getResponse(q)
    print(r)