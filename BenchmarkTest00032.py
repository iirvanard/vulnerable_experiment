import sqlite3
from flask import Flask, request, render_template, make_response
from werkzeug.exceptions import BadRequest
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    """Mendapatkan koneksi database SQLite (ganti sesuai DB yang digunakan)."""
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sqli-00/BenchmarkTest00032", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return render_template("benchmark_form.html")  # Gunakan template untuk form

    response = make_response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest00032", "").strip()

    if not param:
        response.set_data("Error: Password tidak boleh kosong.")
        response.status_code = 400
        return response

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Gunakan parameterized query untuk mencegah SQL Injection
        sql = "SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?"
        cursor.execute(sql, ("foo", param))
        result = cursor.fetchone()

        conn.close()

        if result:
            response.set_data("Login berhasil!")
        else:
            response.set_data("Login gagal. Periksa kembali username dan password.")

    except sqlite3.Error as e:
        response.set_data("Error processing request.")
        response.status_code = 500

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
