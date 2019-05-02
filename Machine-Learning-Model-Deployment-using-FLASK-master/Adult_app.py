# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 23:30:02 2019

@author: INTEL
"""
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/index')
def adult():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
#url = 'http://localhost:5000/api'

