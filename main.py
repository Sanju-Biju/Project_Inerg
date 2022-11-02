import flask
from flask import request, jsonify
import json
import sqlite3 as lite

app = flask.Flask(__name__)
conn = lite.connect('database.db')
cur = conn.cursor()




@app.route('/all', methods=['GET'])
def api_all():
    conn = lite.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM wells')
    wells = cur.fetchall()
    return jsonify(wells)

@app.route('/well/<str>', methods=['GET'])
def api_well(str):
    conn = lite.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM wells WHERE well_number = ?', (str,))
    rows = cur.fetchall()
    return jsonify(rows)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
   