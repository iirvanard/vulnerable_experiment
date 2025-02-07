
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-00/BenchmarkTest00003", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("BenchmarkTest00003.html"))
        user_cookie = make_response()
        user_cookie.set_cookie('BenchmarkTest00003', 'someSecret', max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie('BenchmarkTest00003', value='someSecret', max_age=60 * 3, secure=True, path=request.path, domain=request.host)

        return response

    if request.method == 'POST':
        response_text = ""
        param = "noCookieValueSupplied"

        the_cookies = request.cookies
        if 'BenchmarkTest00003' in the_cookies:
            param = the_cookies['BenchmarkTest00003']

        try:
            algorithm = 'SHA512'  # Placeholder for properties loading
            if algorithm not in ['SHA512', 'SHA256', 'SHA1']:  # Example, extend as needed
                algorithm = 'SHA512'
            import hashlib
            md = hashlib.new(algorithm)
            input_data = bytearray(b'?')

            if isinstance(param, str):
                input_data = param.encode()

            md.update(input_data)

            result = md.digest()
            file_target = os.path.join('path_to_your_test_directory', 'passwordFile.txt')

            with open(file_target, 'a') as fw:
                fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

            response_text += f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

        except Exception as e:
            print("Problem executing hash - TestCase")
            raise e

        response_text += "Hash Test executed"
        return response_text


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
