
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00034", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.args.get('BenchmarkTest00034', '')

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + param + "'"

        try:
            statement = get_sql_statement()
            statement.execute(sql)
            rows = statement.fetchall()
            # Assuming there's a function to print results
            for row in rows:
                response.data += str(row) + '<br>'
            return response
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
