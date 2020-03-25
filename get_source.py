import requests 

def connect_source():
    url = "https://www.worldometers.info/coronavirus/"
    print("CONNECTING ...")
    r = requests.get(url)

    print("State : ", r.status_code)
    if (r.status_code == 200):
        print('\x1b[5;30;42m' + 'CONNECTION ESTABLISED' + '\x1b[0m')
    else:
        print("FAILED! ")
    print("........................ ")
    print(r.headers['content-type'])
    print(".........................")
    print(f"Encoding: {r.encoding}")
    print("........................ \n")

    return r 

