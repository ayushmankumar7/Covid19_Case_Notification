import google.cloud
import serial
import firebase_admin
import time
import datetime
import ast
from firebase_admin import firestore
from firebase_admin import credentials

def send_it(data, firebase_admin = firebase_admin, credentials = credentials, firestore = firestore):
	if (not len(firebase_admin._apps)):
		
		cred = credentials.Certificate("question-us-firebase-adminsdk-92oz0-fb023cef4f.json")

		default_app = firebase_admin.initialize_app(cred,
			{'projectID': 'question-us'
			})

	db = firestore.client()

	ref = db.collection(u'covid_19')

	try:
		docs = ref.get()
		for doc in docs:
			print(u'Doc Data:{}'.format(doc.to_dict()))
	except google.cloud.exceptions.NotFound:
		print(u'Missing data')
		
	
	ref.document("R7kgT8f7Rj4BzseYvG0t").set({u'International':data})

