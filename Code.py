from flask import Flask,jsonify,request

app=Flask(__name__)

datas=[

{

    'id':1,
    'contact':'1672864567',
    'name':'Raju',
    'done':False
},

{

    'id':2,
    'contact':'9175243816',
    'name':'Rahul',
    'done':False
},

]

@app.route('/')
def sample():
    return ' Contact '

@app.route("/add-data",methods=["POST"])
def addData():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the Data"
        },400)

    contact={
        'id':datas[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }

    datas.append(contact)

    return jsonify({
        'status':'Succcess',
        'message':'data added successfully'
    })


@app.route('/get-data')
def getData():
    return jsonify({
        'data':datas
    })

if (__name__=='__main__'):
    app.run(debug=True)

