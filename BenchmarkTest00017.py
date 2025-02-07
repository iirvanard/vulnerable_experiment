import os
import urllib.parse
import shlex
import subprocess
from flask import Flask, request, render_template, make_response
from markupsafe import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00017", methods=['GET', 'POST'])
def benchmark_test_00017():
    return benchmark_test_00017_post()

def benchmark_test_00017_post():
    response = make_response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    # Ambil header secara aman
    param = request.headers.get("BenchmarkTest00017", "").strip()
    param = urllib.parse.unquote(param)

    # Validasi input: hanya huruf, angka, spasi, dan beberapa simbol
    if not param.isascii() or ";" in param or "&" in param or "|" in param:
        response.set_data("Invalid input.")
        response.status_code = 400
        return response

    # Tentukan perintah yang aman
    if os.name == 'nt':  # Windows
        cmd = ["cmd", "/c", "echo", param]
    else:  # Linux/MacOS
        cmd = ["echo", param]

    try:
        # Gunakan subprocess dengan list untuk menghindari command injection
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        safe_output = escape(result.stdout)  # Hindari XSS
        response.set_data(safe_output)

    except subprocess.CalledProcessError as e:
        response.set_data("Command execution failed.")
        response.status_code = 500

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
