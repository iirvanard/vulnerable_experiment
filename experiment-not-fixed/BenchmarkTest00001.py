
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00001", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00001.html"))
        user_cookie = ('BenchmarkTest00001', 'FileName', {'max_age': 60 * 3, 'secure': True,
                                                           'path': request.path,
                                                           'domain': request.host})
        response.set_cookie(*user_cookie)
        return response
    else:
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if 'BenchmarkTest00001' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00001'])

        file_name = None
        try:
            file_name = os.path.join('path/to/test/files', param)  # Adjust the path accordingly
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                return f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
        except Exception as e:
            print(f"Couldn't open FileInputStream on file: '{file_name}'")
            return f"Problem getting FileInputStream: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
