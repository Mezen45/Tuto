from flask import Flask, jsonify, request
app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello guys"


@app.route('/hithere')
def hithere_everyone():
    return "Hello Again"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]

    z = x+y

    retJson= {
       "z":z
    }

    return jsonify(retJson), 200




@app.route('/bye')
def bye():
    age= 2*5

#    c = 1/0
    retJson = {
    'Name':'Mezen',
    'Age':age,
    "phones":[
        {
            "phoneName":"Iphone",
            "phoneNumber":11111
      },
       {
       "phoneName":"Nokia",
       "phoneNumber":11121
       }
       ]
    }
    return jsonify(retJson)

if __name__=="__main__":
    app.run(debug=True)
