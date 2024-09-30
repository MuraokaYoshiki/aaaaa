# -*- coding: utf-8 -*-
# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash
from io import TextIOWrapper
import csv
from MyDatabase import get_user_role, my_open, my_query, my_close

app = Flask(__name__, static_folder="static")
app.secret_key = 'your_secret_key'

dsn = {
    'host': '172.30.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'dbron110'
}

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        role = get_user_role(username)
        if (role == '管理者'):
            create_admin_tables()  # 管理者用のテーブルを作成または更新
            return render_template('admin_index.html', username=username)
        else:
            return render_template('index.html', username=username)
    return redirect(url_for('login'))

def my_query(query, cur):
    cur.execute(query)

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

@app.route('/upload_record', methods=['POST'])
def upload_record():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    file = request.files['file']
    if not file:
        flash('ファイルが選択されていません。')
        return redirect(url_for('index'))
    
    stream = TextIOWrapper(file.stream, encoding='utf-8')
    reader = csv.reader(stream)
    
    dbcon, cur = my_open(**dsn)
    
    # Skip the first line (header)
    next(reader, None)
    
    username = session['username']  # 現在ログイン中のユーザーIDを取得
    
    for row in reader:
        try:
            month = int(row[0])         # Assuming '日付(月)' is the first column
            day = int(row[1])           # Assuming '日付(日)' is the second column
            time = row[2]               # Assuming '時間(AMまたはPMと入力)' is the third column
            temperature = float(row[3])  # Assuming '体温(℃)' is the fourth column
            joint_pain = parse_boolean(row[4])     # Assuming '関節・筋肉痛(ある場合は"有"と記入)' is the fifth column
            malaise = parse_boolean(row[5])        # Assuming 'だるさ(ある場合は"有"と記入)' is the sixth column
            headache = parse_boolean(row[6])       # Assuming '頭痛(ある場合は"有"と記入)' is the seventh column
            sore_throat = parse_boolean(row[7])    # Assuming '咽頭痛(ある場合は"有"と記入)' is the eighth column
            shortness_breath = parse_boolean(row[8])   # Assuming '息苦しさ(ある場合は"有"と記入)' is the ninth column
            cough = parse_boolean(row[9])         # Assuming '咳・くしゃみ(ある場合は"有"と記入)' is the tenth column
            nausea = parse_boolean(row[10])       # Assuming '吐気・嘔吐(ある場合は"有"と記入)' is the eleventh column
            abdominal_pain = parse_boolean(row[11])   # Assuming '腹痛・下痢(ある場合は"有"と記入)' is the twelfth column
            taste_disorder = parse_boolean(row[12])    # Assuming '味覚障害(ある場合は"有"と記入)' is the thirteenth column
            olfactory_disorder = parse_boolean(row[13])    # Assuming '嗅覚障害(ある場合は"有"と記入)' is the fourteenth column
            infection = parse_boolean(row[14])     # Assuming '感染(判明した段階で初日に"有"と記入)' is the fifteenth column
            close_contact = parse_boolean(row[15]) # Assuming '濃厚接触(判明した段階で初日に"有"と記入)' is the sixteenth column
            additional_notes = row[16] if len(row) > 16 else None  # Assuming additional notes
            
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
    
    # Fetch records where there are gaps of 3 or more days between 1/25 and 2/7
    query_notifications = """
        SELECT g.gakuseki_ID, r.months, r.days, "3日以上記入がありません" AS tokkizikou
        FROM (
            SELECT g.gakuseki_ID, r.months, r.days,
                   ROW_NUMBER() OVER (PARTITION BY g.gakuseki_ID ORDER BY r.months, r.days) AS rn
            FROM records r
            JOIN gakusekiss g ON r.gakuseki_ID = g.gakuseki_ID
            WHERE r.months BETWEEN 1 AND 2 AND r.days BETWEEN 25 AND 7
        ) AS sub
        WHERE rn >= 3
    """
    cur.execute(query_notifications)
    notifications = cur.fetchall()
    
    my_close(dbcon, cur)
    
    return render_template('admin_index.html', username=session['username'], notifications=notifications)

def create_admin_tables():
    dbcon, cur = my_open(**dsn)
    
    # Create or update admin-specific tables if necessary
    create_health_records_table = """
        CREATE TABLE IF NOT EXISTS health_records (
            health_record_ID INT AUTO_INCREMENT PRIMARY KEY,
            gakuseki_ID VARCHAR(255),
            months INT,
            days INT,
            zikan VARCHAR(255),
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
            infection BOOLEAN,
            close_contact BOOLEAN
        )
    """
    
    create_infection_records_table = """
        CREATE TABLE IF NOT EXISTS infection_records (
            infection_record_ID INT AUTO_INCREMENT PRIMARY KEY,
            gakuseki_ID VARCHAR(255),
            infection_date DATE,
            infection_type VARCHAR(255)
            )
    """
    
    create_notifications_table = """
        CREATE TABLE IF NOT EXISTS notifications (
            notification_ID INT AUTO_INCREMENT PRIMARY KEY,
            gakuseki_ID VARCHAR(255),
            notification_message TEXT
        )
    """
    
    my_query(create_health_records_table, cur)
    my_query(create_infection_records_table, cur)
    my_query(create_notifications_table, cur)
    
    my_close(dbcon, cur)

if __name__ == '__main__':
    app.run(debug=True)


