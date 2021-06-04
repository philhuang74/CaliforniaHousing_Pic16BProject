from flask import Blueprint, g, render_template, abort
import sqlite3

def get_hw_db():
    if 'hw_db' not in g:
        g.hw_db = sqlite3.connect('housing.sqlite')

    return g.hw_db

def close_hw_db(e=None):
    db = g.pop('hw_db', None)

    if db is not None:
        db.close()

housewares_bp = Blueprint('housewares', __name__, url_prefix='/housewares')

@housewares_bp.route('/')
def list():
    db = get_hw_db()
    c = db.cursor()
    c.execute("SELECT DISTINCT Zip FROM housing")
    result = [elem[0] for elem in c.fetchall()]
    return render_template('housewares/list.html', housewares=result)

@housewares_bp.route('/<name>')
def display(name):
    try:
        db = get_hw_db()
        c = db.cursor()
        # use prepared statements for safety
        c.execute(f"SELECT DISTINCT Latitude FROM housing WHERE Name=?", (name,))
        variations = [elem[0] for elem in c.fetchall()]
        c.execute(f"SELECT DISTINCT Longitude FROM housing WHERE Name=?", (name,))
        diy = c.fetchall()[0][0]
        c.execute(f"SELECT DISTINCT RegionID FROM housing WHERE Name=?", (name,))
        buy = c.fetchall()[0][0]
        c.execute(f"SELECT DISTINCT SizeRank FROM housing WHERE Name=?", (name,))
        sell = c.fetchall()[0][0]
        return render_template('housewares/display.html', name=name, variations=variations, diy=diy, buy=buy, sell=sell)
    except:
        abort(404)
