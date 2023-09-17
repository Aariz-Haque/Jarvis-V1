import hashlib
import pyautogui

def validateUser():
    h=hashlib.new("SHA256")
    password=pyautogui.password(text="Enter your password")
    h.update(password.encode())
    passwordHash=h.hexdigest()
    with open("Security\\passwordHash.txt",'r') as f:
        correctHash=f.read()
    if passwordHash==correctHash:
        return True
    else:
        return False
