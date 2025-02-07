
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00030", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    values = request.values.getlist('BenchmarkTest00030')
    if values:
        param = values[0]

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.data = response.get_data(as_text=True) % tuple(obj)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
