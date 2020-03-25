from bs4 import BeautifulSoup
from get_source import connect_source

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
