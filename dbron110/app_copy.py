import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import csv
from werkzeug.utils import secure_filename
from MyDatabase import get_user_role, my_open, my_query, my_close

app = Flask(__name__, static_folder="static")
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = '/path/to/uploads'  # Set your upload folder here

dsn = {
    'host': '172.30.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'dbron110'
}

def my_query(query, cur):
    cur.execute(query)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        role = get_user_role(username)
        if role == '管理者':
            create_admin_tables()  # Create or update admin tables
            return render_template('admin_index.html', username=username)
        else:
            return render_template('index.html', username=username)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        dbcon, cur = my_open(**dsn)
        query = f"SELECT * FROM gakusekiss WHERE gakuseki_ID='{username}'"
        my_query(query, cur)
        user = cur.fetchone()
        my_close(dbcon, cur)
        
        if user:
            if user['loginpass'] == password:
                session['username'] = username
                return redirect(url_for('index'))
            else:
                flash('ユーザー名またはパスワードが間違っています。')
        else:
            session['temp_username'] = username
            session['temp_password'] = password
            return redirect(url_for('register'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = session.get('temp_username')
        password = session.get('temp_password')
        name = request.form['name']
        role = request.form['role']
        email = request.form['email']
        
        dbcon, cur = my_open(**dsn)
        query = f"INSERT INTO gakusekiss (gakuseki_ID, namae, yakuwari, email, loginpass) VALUES ('{username}', '{name}', '{role}', '{email}', '{password}')"
        my_query(query, cur)
        dbcon.commit()
        my_close(dbcon, cur)
        
        session.pop('temp_username', None)
        session.pop('temp_password', None)
        session['username'] = username
        flash('ユーザを登録しました。')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def parse_boolean(value):
    return value == '有'

import io

@app.route('/upload_record', methods=['POST'])
def upload_record():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    file = request.files['csv_file']
    if not file:
        flash('ファイルが選択されていません。')
        return redirect(url_for('index'))
    
    # Open the file in text mode using io.TextIOWrapper
    stream = io.TextIOWrapper(file.stream, encoding='utf-8')
    reader = csv.reader(stream)
    
    dbcon, cur = my_open(**dsn)
    
    # Skip the header row
    next(reader, None)
    
    username = session['username']
    
    for row in reader:
        try:
            month = int(row[0])
            day = int(row[1])
            time = row[2]  #'AM'or'PM'
            temperature = float(row[3])
            joint_pain = parse_boolean(row[4])
            malaise = parse_boolean(row[5])
            headache = parse_boolean(row[6])
            sore_throat = parse_boolean(row[7])
            shortness_breath = parse_boolean(row[8])
            cough = parse_boolean(row[9])
            nausea = parse_boolean(row[10])
            abdominal_pain = parse_boolean(row[11])
            taste_disorder = parse_boolean(row[12])
            olfactory_disorder = parse_boolean(row[13])
            
            query = f"""
                INSERT INTO records (gakuseki_ID, months, days, zikan, bodytemperature, joint_pain, malaise, headache, sore_throat, shortness_breath, Cough, Nausea, Abdominal_pain, Taste_disorder, Olfactory_disorder)
                VALUES ('{username}', {month}, {day}, '{time}', {temperature}, {joint_pain}, {malaise}, {headache}, {sore_throat}, {shortness_breath}, {cough}, {nausea}, {abdominal_pain}, {taste_disorder}, {olfactory_disorder})
            """
            my_query(query, cur)
        except (ValueError, IndexError) as e:
            flash(f'データに不備があります: 不明/{row[1]} エラー: {str(e)}')
            my_close(dbcon, cur)
            return redirect(url_for('index'))
    
    dbcon.commit()
    my_close(dbcon, cur)
    
    flash('記録が正常にアップロードされました。')
    return redirect(url_for('index'))

@app.route('/admin_index')
def admin_index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_role = get_user_role(session['username'])
    if user_role != '管理者':
        flash('管理者権限が必要です。')
        return redirect(url_for('index'))
    
    # Fetch records for notifications
    dbcon, cur = my_open(**dsn)
    
#   # Fetch records where there are gaps of 3 or more days between 1/25 and 2/7
#   query_notifications = """
#       SELECT g.gakuseki_ID, r.months, r.days, "3日以上記入がありません" AS message
#       FROM (
#           SELECT g.gakuseki_ID, r.months, r.days,
#                  ROW_NUMBER() OVER(PARTITION BY r.gakuseki_ID ORDER BY r.months, r.days) AS seqnum
#           FROM gakusekiss g JOIN records r ON g.gakuseki_ID = r.gakuseki_ID
#           WHERE r.months = 1 AND r.days BETWEEN 25 AND 31
#              OR r.months = 2 AND r.days <= 7
#       ) r
#       WHERE seqnum = 1;
#   """
#   
#   my_query(query_notifications, cur)
    notifications = cur.fetchall()
    my_close(dbcon, cur)
    
    return render_template('admin_index.html', notifications=notifications)

def create_admin_tables():
    dbcon, cur = my_open(**dsn)
    
    # Create or update health_records table
    query_health_records = """
        CREATE TABLE IF NOT EXISTS health_records (
            record_ID INT AUTO_INCREMENT PRIMARY KEY,
            gakuseki_ID VARCHAR(10),
            months INT,
            days INT,
            zikan VARCHAR(2),
            bodytemperature FLOAT,
            joint_pain BOOLEAN,
            malaise BOOLEAN,
            headache BOOLEAN,
            sore_throat BOOLEAN,
            shortness_breath BOOLEAN,
            cough BOOLEAN,
            nausea BOOLEAN,
            abdominal_pain BOOLEAN,
            taste_disorder BOOLEAN,
            olfactory_disorder BOOLEAN,
            FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
        )
    """
    my_query(query_health_records, cur)

    # Insert records from records table to health_records table
    query_insert_health_records = """
        INSERT INTO health_records (gakuseki_ID, months, days, zikan, bodytemperature, joint_pain, malaise, headache, sore_throat, shortness_breath, cough, nausea, abdominal_pain, taste_disorder, olfactory_disorder)
        SELECT gakuseki_ID, months, days, zikan, bodytemperature, joint_pain, malaise, headache, sore_throat, shortness_breath, cough, nausea, abdominal_pain, taste_disorder, olfactory_disorder
        FROM records
    """
    my_query(query_insert_health_records, cur)
    
#    # Create or update infection_records table
#    query_infection_records = """
#        CREATE TABLE IF NOT EXISTS infection_records (
#            record_ID INT AUTO_INCREMENT PRIMARY KEY,
#            gakuseki_ID VARCHAR(10),
#            months INT,
#            days INT,
#            yakuwari VARCHAR(255),
#            FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
#        )
#    """
#    my_query(query_infection_records, cur)
#
#    # Insert records from records table to infection_records table
#    query_insert_infection_records = """
#        INSERT INTO infection_records (gakuseki_ID, months, days, yakuwari)
#        SELECT r.gakuseki_ID, r.months, r.days, g.yakuwari
#        FROM records r
#        JOIN gakusekiss g ON r.gakuseki_ID = g.gakuseki_ID
#        WHERE r.infection = TRUE
#    """
#    my_query(query_insert_infection_records, cur)
#    
#    # Create or update notifications table
#    query_notifications = """
#        CREATE TABLE IF NOT EXISTS notifications (
#            notification_ID INT AUTO_INCREMENT PRIMARY KEY,
#            gakuseki_ID VARCHAR(10),
#            months INT,
#            days INT,
#            message VARCHAR(255),
#            FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
#        )
#    """
#    my_query(query_notifications, cur)
#    
#    # Insert notifications for gaps of 3 or more days between 1/25 and 2/7
#    query_insert_notifications = """
#        INSERT INTO notifications (gakuseki_ID, months, days, message)
#        SELECT gakuseki_ID, months, days, "3日以上記入がありません"
#        FROM (
#            SELECT gakuseki_ID, months, days,
#                   ROW_NUMBER() OVER(PARTITION BY gakuseki_ID ORDER BY months, days) AS seqnum
#            FROM records
#            WHERE (months = 1 AND days BETWEEN 25 AND 31)
#               OR (months = 2 AND days <= 7)
#        ) r
#        WHERE seqnum = 1
#    """
#    my_query(query_insert_notifications, cur)
#    
    dbcon.commit()
    my_close(dbcon, cur)

if __name__ == '__main__':
    app.run(debug=True)
