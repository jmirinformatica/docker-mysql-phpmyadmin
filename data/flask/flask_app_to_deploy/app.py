from flask import Flask
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)

app.config['MYSQL_HOST'] = Config.FLASK_MYSQL_HOST
app.config['MYSQL_PORT'] = Config.FLASK_MYSQL_PORT
app.config['MYSQL_USER'] = Config.FLASK_MYSQL_USER
app.config['MYSQL_PASSWORD'] = Config.FLASK_MYSQL_PASSWORD
app.config['MYSQL_DB'] = Config.FLASK_MYSQL_DATABASE

mysql = MySQL(app)

@app.route('/')
def demo():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT NOW()''')
    data = cur.fetchall()
    cur.close()
    return f"<h1>Hello from Flask!</h1><p>{data}</p><img src='/static/mei.png' alt='mei'>"