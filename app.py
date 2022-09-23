from flask import Flask, render_template
import sqlite3
import os


#Create a new Flask instance
app = Flask(__name__)


#define a function that is called when a user visits the root of the website
def get_db_connection():
    dir = os.getcwd() + "/Database/patient.db"
    print('dir: ', dir)
    conn = sqlite3.connect(dir) #connect to the database
    conn.row_factory = sqlite3.Row #return rows that behave like dictionaries
    return conn



#Create some basic routes
@app.route('/patients')
def index():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql: ', patientListSql)
    return render_template('index.html', list_patients=patientListSql)

@app.route('/patients_bootstrap')
def bootstrap():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql: ', patientListSql)
    return render_template('bootstrap_patients.html', list_patients=patientListSql)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)