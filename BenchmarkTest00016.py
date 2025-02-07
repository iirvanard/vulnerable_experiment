
import os
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00016", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = ""
    headers = request.headers.getlist("BenchmarkTest00016")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    if param == "":
        param = "No cookie value supplied"

    response.set_cookie('SomeCookie', param, secure=True, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{param}' and secure flag set to: true"
    response.content_type = "text/html;charset=UTF-8"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
