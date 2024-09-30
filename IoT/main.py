import flask
import mysql.connector

app = flask.Flask(__name__)

# Easy API
@app.route("/")
def hello():
    print("API Called")
    return "Hello Flask"

# Function to insert number into database
def insert_into_db(id, type, value):
    # Connect to database
    context = mysql.connector.connect(user="app", password="Abcde123")
    cursor = context.cursor()

    # Enforce SQL using number getting from JSON
    cursor.execute("INSERT INTO iot.value VALUES (%s,%s,%s,now())", (id, type, value))
    context.commit()

    # Cleaning up
    cursor.close()
    context.close()

# API to get JSON data
@app.route("/value", methods=['POST'])
def value():
    id = flask.request.json["id"]
    type = flask.request.json["type"]
    value = flask.request.json["value"]
    print("API Called (%s, %s, %s)" % (id, type, value))

    # Insert the number into database
    insert_into_db(id, type, value)

    return "OK!"

# Web page
@app.route("/data", methods=['GET', 'POST'])
def data():
    if flask.request.method == 'POST':
        data_type = flask.request.form.get('data_type', 'light')
        limit = int(flask.request.form.get('limit', 10))
    else:
        data_type = flask.request.args.get('data_type', 'light')
        limit = int(flask.request.args.get('limit', 10))

    # Connect to database
    context = mysql.connector.connect(user="app", password="Abcde123")
    cursor = context.cursor()

    # Enforce SQL to get
    query = "SELECT * FROM iot.value WHERE type=%s ORDER BY time DESC LIMIT %s"
    cursor.execute(query, (data_type, limit))
    items = cursor.fetchall()

    # Cleaning up
    cursor.close()
    context.close()

    return flask.render_template("data1.html", name="Room 115", items=items, data_type=data_type, limit=limit)

# Enforce the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)