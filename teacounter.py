from flask import Flask
import json
app = Flask(__name__)

teateas=[]

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
