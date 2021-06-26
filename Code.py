from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [
    { 
    "Contact": "9678547865", 
    "name": 'Nathan', 
    'done': False, 
    'id': 1
    }, 
    { 
    'Contact': "8974458950", 
    'name': 'Ryan', 
    'done': False, 
    'id': 2
    }
]

@app.route("/add_data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Pls provide the data!",
        },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status" : "success",
        "message" : "Task added successfully!",
    })

@app.route("/get_data")
def get_task():
    return jsonify({
        "data" : tasks
    })

if __name__ == "__main__":
    app.run() 