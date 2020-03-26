# Covid19_Case_Notification
This a Python script which gives live updates on New Covid19 patients in a Particular country(here India by default)


## Steps to Follow

### > Linux

```shell
$ sudo apt install python-gi gir1.2-notify-0.7

$ pip3 install beautifulsoup4

$ python3 main.py

```
### > Windows

```shell
$ pip install win10toast

$ pip install requests

$ pip install beautifulsoup4

$ python main.py

```

## Current State

### > Terminal
![](images/currentState.png)

### > Notification
![](images/Notification.png)

## Tree

```shell
.
├── app
│   ├── flask_app.py
│   └── __pycache__
│       └── flask_app.cpython-36.pyc
├── extras
│   ├── index.html
│   ├── main.js
│   └── style.css
├── images
│   ├── currentState.png
│   ├── Notification.png
│   └── techStack.png
├── LICENSE
├── main.py
├── question-us-firebase-adminsdk-92oz0-fb023cef4f.json
├── README.md
├── src
│   ├── database
│   │   ├── firestore_connect.py
│   │   ├── __pycache__
│   │   │   └── firestore_connect.cpython-36.pyc
│   │   └── question-us-firebase-adminsdk-92oz0-fb023cef4f.json
│   ├── get_source.py
│   ├── notification
│   │   ├── notify_linux.py
│   │   ├── notify_windows.py
│   │   └── __pycache__
│   │       └── notify_linux.cpython-36.pyc
│   └── __pycache__
│       └── get_source.cpython-36.pyc
├── templates
│   └── index.html
└── wsgi.py



```

## Current Technology Stack

![](images/techStack.png)
