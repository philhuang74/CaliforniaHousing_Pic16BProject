from flask import Flask, g, render_template, request
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from .housewares import housewares_bp, close_hw_db
from .auth import auth_bp, close_auth_db, init_auth_db_command
from .queryfunction import query_function
from .create_figures import create_figures

# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

# Create main page (fancy)

@app.route('/')
def main():
    return render_template('main_better.html')

# Show url matching

@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/hello/<name>/')
def hello_name(name):
    return render_template('hello.html', name=name)

# Page with form

@app.route('/ask/', methods=['POST', 'GET'])
def ask():
    if request.method == 'GET':
        return render_template('ask.html')
    else:
        try:
            Q1_ans = request.form['Q1']
            Q2_ans = request.form['Q2']
            Q3_ans = request.form['Q3']
            Q4_ans = request.form['Q4']
            Min_ans = request.form['minb']
            Max_ans = request.form['maxb']
            desired_alldates = query_function(int(Q1_ans),int(Q2_ans),int(Q3_ans),int(Q4_ans),int(Min_ans),int(Max_ans))
            desired = query_function(int(Q1_ans),int(Q2_ans),int(Q3_ans),int(Q4_ans),int(Min_ans),int(Max_ans),True)
            figs = create_figures(desired_alldates)
            return render_template('ask.html',tables=[desired.to_html(classes='data')], titles=desired.columns.values, results=figs)
        except:
            return render_template('ask.html')

# File uploads and interfacing with complex Python

@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            image = request.files['image']
            img = plt.imread(image)
            if img.shape != (28, 28, 3):
                raise Exception('invalid size')

            img = (img[:,:,0] + img[:,:,1] + img[:,:,2])/3
            img = 255*img/np.max(img)
            img = 255 - img

            img = img.reshape((1, 28, 28))
            model = tf.keras.models.load_model('mnist_model')

            d = np.argmax(model.predict(img))

            return render_template('submit.html', digit=d)
        except:
            return render_template('submit.html', error=True)

# Blueprints and interfacing with SQLite

app.register_blueprint(housewares_bp)
app.teardown_appcontext(close_hw_db)

# Sessions and logging in

app.secret_key = b'h\x13\xce`\xd9\xde\xbex\xbd\xc3\xcc\x07\x04\x08\x88~'

app.register_blueprint(auth_bp)
app.teardown_appcontext(close_auth_db)
app.cli.add_command(init_auth_db_command) # run with flask init-auth-db
