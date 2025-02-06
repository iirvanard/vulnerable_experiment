
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00017", methods=['GET', 'POST'])
def benchmark_test_00017():
    if request.method == 'GET':
        return benchmark_test_00017_post()

    return benchmark_test_00017_post()

def benchmark_test_00017_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = ""

    headers = request.headers.getlist("BenchmarkTest00017")
    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "cmd /c echo "  # substitute with appropriate command

    try:
        p = os.popen(cmd + param)
        result = p.read()
        response.set_data(result)
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e).replace("<", "&lt;").replace(">", "&gt;"))
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
