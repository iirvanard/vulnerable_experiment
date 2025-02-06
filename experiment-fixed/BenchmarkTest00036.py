
import os
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00036", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = ""
        flag = True
        names = request.args.keys()
        for name in names:
            values = request.args.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest00036":
                        param = name
                        flag = False
                        break
            if not flag:
                break

        response.headers['X-XSS-Protection'] = '0'
        length = 1
        if param:
            length = len(param)
            response.data = param[:length]
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
