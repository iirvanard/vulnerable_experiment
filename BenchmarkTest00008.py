
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

    # Whitelist stored procedures
    ALLOWED_PROCEDURES = {"safe_proc1", "safe_proc2", "safe_proc3"}

    if param not in ALLOWED_PROCEDURES:
        return "Invalid procedure name.", 400

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()

        query = "CALL %s"
        cursor.execute(query, (param,))


        results = cursor.fetchall()
        return str(results)  # Sesuaikan dengan cara rendering yang diinginkan

    except Exception as e:
        return f"Error processing request: {str(e)}", 500

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
