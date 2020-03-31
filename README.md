# Covid19_Case_Notification
This a Python script which gives live updates on New Covid19 patients in a Particular country(here India by default)


## Steps to Follow

### > Linux

```shell
$ sudo apt install python-gi gir1.2-notify-0.7

$ pip3 install beautifulsoup4

$ python3 main.py

$ pip3 install flask

$ pip3 install firebase-admin

```
### > Windows

```shell
$ pip install win10toast

$ pip install requests

$ pip install beautifulsoup4

$ python main.py

$ pip install flask

$ pip install firebase-admin

```

## Current State

### > Terminal
![](images/currentState.png)

### > Notification

#### > Linux
![](images/Notification.png)
#### > Windows
![](images/windows.png)

## Tree

```shell
.
├── app
│   ├── flask_app.py
│   ├── __pycache__
│   │   └── flask_app.cpython-36.pyc
│   └── templates
│       └── index.html
├── extras
│   ├── index.html
│   ├── main.js
│   └── style.css
├── images
│   ├── currentState.png
│   ├── Notification.png
│   ├── techStack.png
│   └── windows.png
├── LICENSE
├── main.py
├── question-us-firebase-adminsdk-92oz0-fb023cef4f.json
├── README.md
├── run_main.sh
├── src
│   ├── database
│   │   ├── firestore_connect.py
│   │   ├── __pycache__
│   │   │   └── firestore_connect.cpython-36.pyc
│   │   └── question-us-firebase-adminsdk-92oz0-fb023cef4f.json
│   ├── get_source.py
│   ├── MLmodel
│   │   └── data.py
│   ├── notification
│   │   ├── notify_linux.py
│   │   ├── notify_windows.py
│   │   └── __pycache__
│   │       └── notify_linux.cpython-36.pyc
│   └── __pycache__
│       └── get_source.cpython-36.pyc
└── wsgi.py



```

## Current Technology Stack

![](images/techStack.png)
