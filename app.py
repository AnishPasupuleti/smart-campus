from flask import Flask, render_template, request, redirect, send_from_directory
import qrcode, os, sqlite3
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists('database.db'):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE attendance (id INTEGER PRIMARY KEY, name TEXT, time TEXT)')
    c.execute('''CREATE TABLE issues (
        id INTEGER PRIMARY KEY, name TEXT, location TEXT, description TEXT,
        image TEXT, status TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('scan.html')

@app.route('/generate_qr')
def generate_qr():
    data = "smartcampus_attendance"
    img = qrcode.make(data)
    img.save("static/attendance_qr.png")
    return redirect('/')

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    name = request.form['name']
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO attendance (name, time) VALUES (?, ?)', (name, t))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/view_attendance')
def view_attendance():
    conn = sqlite3.connect('database.db')
    rows = conn.execute('SELECT * FROM attendance').fetchall()
    conn.close()
    return render_template('attendance.html', rows=rows)

@app.route('/report_issue')
def report_issue():
    return render_template('report.html')

@app.route('/submit_issue', methods=['POST'])
def submit_issue():
    name = request.form['name']
    location = request.form['location']
    description = request.form['description']
    image = request.files['image']
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO issues (name, location, description, image, status) VALUES (?, ?, ?, ?, ?)',
                 (name, location, description, filename, "New"))
    conn.commit()
    conn.close()
    return redirect('/view_issues')

@app.route('/view_issues')
def view_issues():
    conn = sqlite3.connect('database.db')
    rows = conn.execute('SELECT * FROM issues').fetchall()
    conn.close()
    return render_template('issues.html', rows=rows)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/update_status/<int:issue_id>', methods=['POST'])
def update_status(issue_id):
    new_status = request.form['status']
    conn = sqlite3.connect('database.db')
    conn.execute('UPDATE issues SET status = ? WHERE id = ?', (new_status, issue_id))
    conn.commit()
    conn.close()
    return redirect('/view_issues')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
