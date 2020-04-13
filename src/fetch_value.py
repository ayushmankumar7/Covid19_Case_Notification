from src.get_source import connect_source
from bs4 import BeautifulSoup

def current():
    source = connect_source()

    soup = BeautifulSoup(source.text, 'html.parser')

    tf = soup.findAll('td')

    for i in range(len(tf)):
        if tf[i].text == "India":
            print("India")
            india_total = tf[i+1].text
            break
    active_case = soup.find("div", attrs = {'class':"number-table-main"})
    international = active_case.text

    return international, india_total


