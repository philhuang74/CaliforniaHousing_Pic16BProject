# ******************************************************************************
#  * FILE NAME: __init__.py
#  * DESCRIPTION: This python script is a blueprint that maps the routes
#  *              of the website of our project.
#  ******************************************************************************

from flask import Flask, render_template, request
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
            # upon POST request, get the answers to the questionaire form
            Q1_ans = request.form['Q1']
            Q2_ans = request.form['Q2']
            Q3_ans = request.form['Q3']
            Q4_ans = request.form['Q4']
            Min_ans = request.form['minb']
            Max_ans = request.form['maxb']

            # extract the desired pandas dataframe based on the answers to the questionaire form
            desired = query_function(int(Q1_ans),int(Q2_ans),int(Q3_ans),int(Q4_ans),int(Min_ans),int(Max_ans))
            
            # get the html format of the desired dataset
            desired_html_table = desired.to_html(classes='data', table_id="housing-data",justify="center")
            
            # extract the list of (zip code, figure) tuples corresponding to the desired data
            zip_figures = create_figures(desired)
            
            return render_template('ask.html',table=desired_html_table, zip_figures=zip_figures)
        except:
            return render_template('ask.html')

# Sessions and logging in

app.secret_key = b'h\x13\xce`\xd9\xde\xbex\xbd\xc3\xcc\x07\x04\x08\x88~'

app.register_blueprint(auth_bp)
app.teardown_appcontext(close_auth_db)
app.cli.add_command(init_auth_db_command) # run with flask init-auth-db
