from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def greeting():
	return "Welcome to my app!"

@app.route('/additem/<item>')
def add_item(item=""):
	userOne.list.append(item)
	file = open("todo.txt", "a") 
	file.write(item + "\n")
	file.close()
	return "Successfully added: " + item

@app.route('/getlist')
def print_list():
#	myliststr = ""
#	for item in userOne.list:
#		myliststr += item + "<br>"
	file = open("todo.txt", "r")
	todos = file.read()
	file.close()
	return todos



app.run(debug=True, port=8025, host='0.0.0.0')