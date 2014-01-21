#!/usr/bin/env python
from flask import Flask, render_template, url_for, redirect, request
import os
 
app = Flask(__name__) 
 
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.form
 
    return render_template('index.html')
 
@app.route("/action/<act>")
def action(act):
    print act
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.debug = True
    app.run()
