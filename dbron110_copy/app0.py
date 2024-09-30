from flask import Flask, render_template, request, redirect, url_for, session, flash
from MyDatabase import my_open, my_query, my_close

app = Flask(__name__, static_folder="static")
app.secret_key = 'your_secret_key'

dsn = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'dbron110'
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
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
            if user['loginpass'] == password:  # 修正: user['password'] を user['loginpass'] に変更
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

if __name__ == '__main__':
    app.run(debug=True)
