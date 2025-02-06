
import os
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('benchmark.db')  # Update with your database path
    return conn

@app.route("/sqli-00/BenchmarkTest00008", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.headers.get("BenchmarkTest00008", "")
    param = urllib.parse.unquote(param)

    sql = "{call " + param + "}"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        # Implement a function to print results, adapt according to your needs
        return str(results)  # Replace with actual rendering of results
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
