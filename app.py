import pickle as pkl 
from flask import Flask, render_template, request, url_for, redirect
import numpy as np

app = Flask(__name__,template_folder='C:/Users/laksh/Desktop/Major Project/templates')

@app.route('/')
def index():
    return render_template('before.html')

@app.route('/predict',methods=['POST'])
def predict1():
    d1 = request.form['a']
    d2 = request.form['a1']
    d3 = request.form['a2']
    d4 = request.form['a3']
    d5 = request.form['a4']
    d6 = request.form['a5']
    d7 = request.form['a6']
    d8 = request.form['c']
    d9 = request.form['d']
    d10 = request.form['e']
    d11= request.form['f']
    d12= request.form['g']
    d13= request.form['h']
    d14= request.form['i']
    d15= request.form['j']
    d16= request.form['k']
    d17= request.form['l']

    model = pkl.load(open('model.pkl', 'rb'))

    arr = np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17]])
    pred = model.predict(arr)
    return render_template('after.html', data1=pred[0][0],data2=pred[0][1])

if __name__=='__main__':
    app.run(debug=True)