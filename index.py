
from flask import Flask, request, redirect, url_for, render_template
import psycopg2

app = Flask(__name__)

dsn = "postgresql://postgres:admin@localhost:5432/DB2"
conn = psycopg2.connect(dsn, options="-c client_encoding=UTF8")
conn.autocommit = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    email = request.form['email']
    tel = request.form['tel']



    
    cur = conn.cursor()

    sql_insert_query = """
    INSERT INTO public.users (name, email, tel) 
    VALUES (%s, %s, %s)
    """
    data_to_insert = (request.form['name'], request.form['email'], request.form['tel'])


    cur.execute(sql_insert_query, data_to_insert)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
