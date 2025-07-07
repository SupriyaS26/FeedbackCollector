from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
import csv

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    if message.strip():
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute('INSERT INTO feedback (message) VALUES (?)', (message,))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/admin')
def admin():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT * FROM feedback')
    rows = c.fetchall()
    conn.close()
    return render_template('admin.html', feedback=rows)

@app.route('/export')
def export():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('SELECT * FROM feedback')
    rows = c.fetchall()
    conn.close()
    with open('feedback.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Message'])
        writer.writerows(rows)
    return send_file('feedback.csv', as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
