import os
from bs4 import BeautifulSoup
from src.get_source import connect_source
import platform

source = connect_source()


soup = BeautifulSoup(source.text, 'html.parser')

tf = soup.findAll('td')

for i in range(len(tf)):
    if tf[i].text == "India":
        print("India")
        print(f"Total Cases:{tf[i+1].text} ")
        print(f"New Cases: {tf[i+2].text}")
        print(f"Total Death: {tf[i+3].text}")
        print(f"New Death:{tf[i+4].text} ")
        break
    
print("............................")

active_case = soup.find("div", attrs = {'class':"number-table-main"})
print("International Active Cases: ",active_case.text)

osys = platform.uname()
if osys.system == "Linux":
    from src.notification.notify_linux import sudo_notify
    sudo_notify(f"International Active Cases : {active_case.text}")
if platform.uname().system == "Windows":
    from src.notification.notify_windows import admin_notify
    admin_notify(f"International Active Cases : {active_case.text}")
