from flask import Flask
from flask import render_template


app = Flask(__name__)

tupla = [
        ('BSCS','BSCS70','ACTIVE','READ WRITE'),
        ('OAC','OACDB','ACTIVE','READ WRITE'),
        ('SGA','OACDB','CLOSE','READ WRITE'),
        ('TIMPRO','TIMPRODB','CLOSE','READ WRITE')
]



@app.route('/')
def index():

    return render_template('index.html',tupla=tupla)