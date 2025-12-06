from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="studentdb",   
        user="postgres",        
        password="mypass123",
        port="5432"            
    )
    return conn


@app.route('/')
def index():
    return render_template('student_form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    address = request.form['address']
    std = request.form['std']
    dob = request.form['dob']
    age = request.form['age']
    contact = request.form['contact']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, address, std, dob, age,contact) VALUES (%s, %s, %s, %s, %s,%s)",
        (name, address, std, dob, age,contact)
    )
    conn.commit()
    cur.close()
    conn.close()

    return f"Student {name} added successfully!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/students')
def list_students():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    cur.close()
    return str(rows)   



