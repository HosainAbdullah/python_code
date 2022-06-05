# from asyncio.windows_events import NULL
# from html import entities
# from os import abort
# import queue
# from urllib import response
from venv import create
from flask import Flask
from flask import jsonify
from flask import request
import sqlite3

# from curd.create import createEmp

app = Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# c.execute('''
# CREATE TABLE STUDENTS (id integer,name text , address text)
# ''')
# query='''INSERT INTO STUDENTS VALUES(4,'hosain2121','kjsjksdjk')'''
# c.execute(query)

# print(type(list))


@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    conn=sqlite3.connect("Waseetcom.db")
    conn.row_factory = dict_factory
    c=conn.cursor()
    list = c.execute('''  
     Select * from STUDENTS
     ''').fetchall()
    conn.commit()
    conn.close()


    return jsonify({'emps':list})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    conn=sqlite3.connect("Waseetcom.db")
    conn.row_factory = dict_factory
    c=conn.cursor()
    queue= "SELECT * FROM STUDENTS WHERE id ="+empId+""
    result = c.execute(queue).fetchall()
    conn.commit()
    conn.close()
    if len(result) == 0: return jsonify({'response':'Error'})
    else :   return jsonify({'emp':result})
   


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    FlutterData={
            'id': request.json['id'],
            'name':request.json['name'],
            'address':request.json['address']
    }
    conn=sqlite3.connect("Waseetcom.db")
    c=conn.cursor()
    queue= "UPDATE STUDENTS SET id = '"+str(FlutterData['id'])+"',name ='"+FlutterData['name']+"' , address = '"+FlutterData['address']+"' WHERE id = "+empId+""
    result = c.execute(queue).rowcount
    conn.commit()
    conn.close()
    if result == 0: return jsonify({'response':'Error'})
    else : return jsonify({'response':'Success'})


@app.route('/empdb/employee',methods=['POST'])
def createEmp():
    FlutterData={
            'id': request.json['id'],
            'name':request.json['name'],
            'address':request.json['address']
    }
    conn=sqlite3.connect("Waseetcom.db")
    
    c=conn.cursor()

    query="insert into STUDENTS(id,name,address) VALUES("+str(FlutterData['id'])+",'"+FlutterData['name']+"','"+FlutterData['address']+"')"
    r=c.execute(query)
    conn.commit()
    conn.close()
    if r != NULL : response = {'response':'Success'}
    else:  response = {'response':'Error'}
    return response

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    conn=sqlite3.connect("Waseetcom.db")
    c=conn.cursor()
    queue= "DELETE FROM STUDENTS WHERE id ="+empId+""
    result = c.execute(queue).rowcount
    conn.commit()
    conn.close()
    if result == 0: return jsonify({'response':'Error'})
    else :  return jsonify({'response':'Success'})
