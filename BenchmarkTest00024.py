
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('your_database.db')
    return conn

@app.route("/sqli-00/BenchmarkTest00024", methods=['GET', 'POST'])
def benchmark_test_00024():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00024', '')

        sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + param + "'"

        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            cursor.execute(sql, ('foo',))
            results = cursor.fetchall()
            connection.close()
            return render_template("results.html", results=results)
        except Exception as e:
            return "Error processing request."

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
