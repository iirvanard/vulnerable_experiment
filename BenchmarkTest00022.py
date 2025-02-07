
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00022", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = request.form.get("BenchmarkTest00022", "")

    try:
        md = hashlib.sha256()
        input_data = b'?'
        if isinstance(param, str):
            input_data = param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path_to_your_testfiles_dir', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response = f"Sensitive value '{param}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    return response + "Hash Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
