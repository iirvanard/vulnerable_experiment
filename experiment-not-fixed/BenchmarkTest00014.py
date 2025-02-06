
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00014", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    # some code
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    referer = request.headers.get('Referer')

    if referer:
        param = referer  # just grab the referer header value

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(param % obj)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
