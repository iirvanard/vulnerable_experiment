import os
from flask import Flask, request, render_template, session
from markupsafe import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(24)  # Gunakan secret key untuk keamanan sesi

@app.route("/trustbound-00/BenchmarkTest00031", methods=['GET', 'POST'])
def benchmark_test():
    return handle_request()

def handle_request():
    param = request.args.get("BenchmarkTest00031", "")

    # Simpan di sesi Flask, bukan di request.environ
    session['userid'] = param  

    # Escape output untuk mencegah XSS
    safe_param = escape(param)

    return f"Item: 'userid' with value: '{safe_param}' saved in session."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404  # Tambahkan kode status yang benar

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
