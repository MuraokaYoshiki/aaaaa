import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import csv
from werkzeug.utils import secure_filename
from MyDatabase import get_user_role, my_open, my_query, my_close

from datetime import datetime, timedelta

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

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        role = get_user_role(username)
        if role == '管理者':
            create_admin_tables()  # Create or update admin tables
            return redirect(url_for('admin_index'))  # 管理者ページにリダイレクト
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
            infection = parse_boolean(row[14])
            close_contact = parse_boolean(row[15])
            
            query = f"""
                INSERT INTO records (gakuseki_ID, months, days, zikan, bodytemperature, joint_pain, malaise, headache, sore_throat, shortness_breath, Cough, Nausea, Abdominal_pain, Taste_disorder, Olfactory_disorder, infection, close_contact)
                VALUES ('{username}', {month}, {day}, '{time}', {temperature}, {joint_pain}, {malaise}, {headache}, {sore_throat}, {shortness_breath}, {cough}, {nausea}, {abdominal_pain}, {taste_disorder}, {olfactory_disorder}, {infection}, {close_contact})
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

# app.py

@app.route('/admin_index')
def admin_index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_role = get_user_role(session['username'])
    if user_role != '管理者':
        flash('管理者権限が必要です。')
        return redirect(url_for('index'))
    
    create_admin_tables()  # Create or update admin tables
    
    # Fetch records for notifications after creating admin tables
    dbcon, cur = my_open(**dsn)
    query_fetch_notifications = """
        SELECT n.notification_ID, n.gakuseki_ID, n.date, g.namae, g.email
        FROM notifications n
        JOIN gakusekiss g ON n.gakuseki_ID = g.gakuseki_ID
    """
    my_query(query_fetch_notifications, cur)

    notifications = cur.fetchall()
    my_close(dbcon, cur)
    
    print("Fetched notifications:", notifications)
    
    return render_template('admin_index.html', notifications=notifications)
# 新しい関数を追加して、create_admin_tablesの後に実行されることを確認する
@app.after_request
def after_request(response):
    if request.endpoint == 'admin_index':
        create_admin_tables()
    return response

def create_admin_tables():
    dbcon, cur = my_open(**dsn)

    # Drop existing tables if they exist
    drop_health_records = "DROP TABLE IF EXISTS health_records"
    drop_infection_records = "DROP TABLE IF EXISTS infection_records"
    drop_notifications = "DROP TABLE IF EXISTS notifications"
    
    my_query(drop_health_records, cur)
    my_query(drop_infection_records, cur)
    my_query(drop_notifications, cur)
    
    dbcon.commit()
    
    # Create or update health_records table
    query_health_records = """
        CREATE TABLE IF NOT EXISTS health_records (
            record_ID INT AUTO_INCREMENT PRIMARY KEY,
            gakuseki_ID VARCHAR(15) NOT NULL,
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
        INSERT INTO health_records (gakuseki_ID, months, days, zikan, bodytemperature,
                                    joint_pain, malaise, headache, sore_throat,
                                    shortness_breath, cough, nausea, abdominal_pain,
                                    taste_disorder, olfactory_disorder)
        SELECT r.gakuseki_ID, r.months, r.days, r.zikan, r.bodytemperature,
               r.joint_pain, r.malaise, r.headache, r.sore_throat,
               r.shortness_breath, r.Cough, r.Nausea, r.Abdominal_pain,
               r.Taste_disorder, r.Olfactory_disorder
        FROM records r
        LEFT JOIN health_records hr ON r.gakuseki_ID = hr.gakuseki_ID
                                   AND r.months = hr.months
                                   AND r.days = hr.days
        WHERE hr.record_ID IS NULL
    """
    my_query(query_insert_health_records, cur)

    # Create or update infection_records table
    query_infection_records = """
    CREATE TABLE IF NOT EXISTS infection_records (
        record_ID INT AUTO_INCREMENT PRIMARY KEY,
        gakuseki_ID VARCHAR(15),
        months INT,
        days INT,
        yakuwari ENUM('感染', '濃厚接触'),
        FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
    )
"""
    my_query(query_infection_records, cur)    
    # Insert records from records table to infection_records table
    query_insert_infection_records = """
    INSERT INTO infection_records (gakuseki_ID, months, days, yakuwari)
    SELECT g.gakuseki_ID, r.months, r.days, '感染'
    FROM records r
    LEFT JOIN gakusekiss g ON r.gakuseki_ID = g.gakuseki_ID
    WHERE r.infection = 1
    AND '感染' NOT IN (
        SELECT yakuwari
        FROM infection_records ir
        WHERE r.gakuseki_ID = ir.gakuseki_ID
            AND r.months = ir.months
            AND r.days = ir.days
      )
"""
    my_query(query_insert_infection_records, cur)

    query_insert_infection_records = """
    INSERT INTO infection_records (gakuseki_ID, months, days, yakuwari)
    SELECT g.gakuseki_ID, r.months, r.days, '濃厚接触'
    FROM records r
    LEFT JOIN gakusekiss g ON r.gakuseki_ID = g.gakuseki_ID
    WHERE r.close_contact = 1
    AND '濃厚接触' NOT IN (
        SELECT yakuwari
        FROM infection_records ir
        WHERE r.gakuseki_ID = ir.gakuseki_ID
            AND r.months = ir.months
            AND r.days = ir.days
      )
"""
    my_query(query_insert_infection_records, cur)
    # Create or update notifications table
    query_notifications = """
    CREATE TABLE IF NOT EXISTS notifications (
        notification_ID INT AUTO_INCREMENT PRIMARY KEY,
        gakuseki_ID VARCHAR(15),
        date DATE,
        namae VARCHAR(255),
        email VARCHAR(255),
        FOREIGN KEY (gakuseki_ID) REFERENCES gakusekiss(gakuseki_ID)
    )
    """ 
    my_query(query_notifications, cur)

    dbcon.commit()

    # Insert notifications for users with no records in the past three days
    now = datetime.now()
    three_days_ago = now - timedelta(days=3)
    
    query_insert_notifications = f"""
    INSERT INTO notifications (gakuseki_ID, date, namae, email)
    SELECT g.gakuseki_ID, CURDATE(), g.namae, g.email
    FROM gakusekiss g
    LEFT JOIN records r ON g.gakuseki_ID = r.gakuseki_ID
        AND r.months = MONTH(CURDATE())
        AND r.days BETWEEN DAY(CURDATE())-3 AND DAY(CURDATE())-1
    GROUP BY g.gakuseki_ID
    HAVING COUNT(r.record_ID) = 0
"""
    my_query(query_insert_notifications, cur)
    dbcon.commit()

    print("Admin tables created and notifications inserted")

    my_close(dbcon, cur)

if __name__ == '__main__':
    app.run(debug=True)