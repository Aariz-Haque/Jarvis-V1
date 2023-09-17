from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import track
warnings.simplefilter("ignore")
Link="https://gpt4login.com/use-chatgpt-online-free/"
console=Console()
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


# console.print("[bold][green]Loading...[/][/]")
for _ in track(range(100),description="[bold][green]Loading...[/][/]"):
    sleep(0.001)
text="""# Welcome to J.A.R.V.I.S """
md=Markdown(text)
console.print(md)
fileWriter(data='3')
