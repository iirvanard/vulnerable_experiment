
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00009", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""

    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection']:
            continue

        param = name
        break

    md = hashlib.sha384()

    input_data = b'?'
    if isinstance(param, str):
        input_data = param.encode()

    md.update(input_data)

    result = md.digest()

    file_target = os.path.join('testfiles', 'passwordFile.txt')
    with open(file_target, 'a') as fw:
        fw.write(f"hash_value={base64.b64encode(result).decode()}\n")

    response += f"Sensitive value '{param}' hashed and stored<br/>"
    response += "Hash Test executed"

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
