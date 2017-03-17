from flask import Flask
import json
import schedule
import time

app = Flask(__name__)

teas=[]
def clearteas():
    global teas
    teas=[]
    return

schedule.every().day.at("03:30").do(clearteas)
schedule.every().day.at("09:00").do(clearteas)

@app.route('/clear')
def clear():
    global teas
    teas=[]
    return "list cleared"

@app.route('/mytea/<name>')
def countme(name):
    global teas
    teas.append(name)
    return name+" your tea added successfully"
    
@app.route('/tealist')
def listtea():
    return json.dumps(teas)


if __name__ == "__main__":
    app.run()
