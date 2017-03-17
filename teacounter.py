from flask import Flask
import json
import schedule
import time

app = Flask(__name__)

teateas=[]

def clearteateas():
    global teateas
    teateas=[]

schedule.every().day.at("03:30").do(clearteateas)
schedule.every().day.at("09:00").do(clearteateas)

@app.route('/countme/<name>')
def countme(name):
    global teateas
    teateas.append(name)
    return name+" your tea added successfully"
@app.route('/listtea')
def listtea():
    return json.dumps(teateas)


if __name__ == "__main__":
    app.run()
