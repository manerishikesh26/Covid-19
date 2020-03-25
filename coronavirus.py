from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message): #this method will provide notifications
    notification.notify(
        title = title,
        message = message,  
        app_icon=(r"C:\Users\rushikesh.mane\Downloads\corona.ico"), #.ico because plyer accepts only .ico it doesnt accept .png or others and mention your own file path
        timeout = 5
    )

def getdata(url): #this method will convert the frontend data of a website into text format for u 
    r = requests.get(url)
    return r.text

if __name__=="__main__":
    myHtmlData = getdata('https://www.mohfw.gov.in/') #website from where we will be taking data
    soup = BeautifulSoup(myHtmlData, 'html.parser') 

    myDataStr =""
    for tr in soup.find_all('tbody')[7].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemList=myDataStr.split("\n\n")

    states = ['Maharashtra', 'Rajasthan'] #list all the states u want to get notified
    for item in itemList[0:24]:
        dataList = item.split('\n')
        if dataList[1] in states:
            #print(dataList)
            nTitle = 'Cases of Covid-19'
            nText = f"State :- {dataList[1]} \nIndian :- {dataList[2]} \nForeign :- {dataList[3]}  \nCured :- {dataList[4]}  \nDeaths :- {dataList[5]}"
            notifyme(nTitle, nText)
            time.sleep(2)


    
