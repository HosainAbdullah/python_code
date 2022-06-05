from os import abort
from urllib import response
from flask import Flask
from flask import jsonify
from flask import request
import sqlite3

def createEmp():
    FlutterData={
             'id': request.json['id'],
            'name':request.json['name'],
            'address':request.json['address']
    }
    print(FlutterData['id'])
    print(FlutterData['name'])
    print(FlutterData['address'])
    conn=sqlite3.connect("Waseetcom.db")
    c=conn.cursor()
    # query='INSERT INTO STUDENTS(id , name ,address) VALUES('+4+',"djdjjdjdj","hhdhhddjd",)'
    # query="INSERT INTO STUDENTS VALUES(4,"+FlutterData["name"]+","+FlutterData["address"]+")"
    # print(jsonify(c.execute(query)))
    query='''INSERT INTO STUDENTS VALUES(5,'hosain ali','yem')'''
    c.execute(query)
    response = 'True'
    # c.execute(query)
    conn.commit()
    return response
    # return jsonify(dat)
#