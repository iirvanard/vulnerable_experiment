
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00013", methods=['GET', 'POST'])
def benchmark_test():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'Referer' in request.headers:
        param = request.headers['Referer']  # grab first element

    param = urllib.parse.unquote(param)  # URL Decode the header value
    response.headers['X-XSS-Protection'] = '0'

    obj = ["a", "b"]
    response.set_data(response.get_data_format(param, obj))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
