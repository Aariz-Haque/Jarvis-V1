from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
warnings.simplefilter("ignore")
Link="https://gpt4login.com/use-chatgpt-online-free/"
# chrome_driver_path = 'Brain\\chromedriver.exe'
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(Link)
def fileReader():
    file = open("Chatnumber.txt","r")
    data = file.read()
    file.close()
    return data

def fileWriter(data):
    file = open("Chatnumber.txt","w")
    file.write(data)
    file.close()

def getResponse(query):
    Query = str(query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(fileReader())
    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass


    AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
    answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    fileWriter(data=str(NewData))
    return answer

print("Starting The GPT4-Model.")
fileWriter(data='3')
# initPrompt="From now on respond to me like you are Cherus. Cherus is an alien from the planet Y-32b and he is very smart and knows a lot about current affairs, space, science, technology etc. Respond in short texts like an Instagram message"
# ChatGPTBrain(Query=initPrompt)
# while True:
#     query=input("Enter query:")
#     res=ChatGPTBrain(Query=query)
#     print(res)
# while True:
        
#     try:
#         file=open("..\\Body\\SpeechRecognition.txt","r")
#         query=file.read()
#         file.close()
#         fileHistory=open("history.txt","r")
#         dataHistory=fileHistory.read()
#         fileHistory.close()

#         if str(query)==str(dataHistory):
#             sleep(0.5)
            
#         else:
#             if query=="__exit__":
#                 exit()
#             else:
#                 result=ChatGPTBrain(Query=query)
#                 speak(result)
#                 print(result)
#                 fileHistory=open("history.txt","w")
#                 fileHistory.write(query)
#                 fileHistory.close()
#     except Exception as e:
#         print(e)