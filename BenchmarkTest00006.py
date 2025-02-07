
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00006", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'

    param = request.headers.get("BenchmarkTest00006", "")
    param = os.path.splitext(param)[0]  # Simulating URL Decode

    arg_list = []

    os_name = os.name
    if os_name == 'nt':
        arg_list.append("cmd.exe")
        arg_list.append("/c")
    else:
        arg_list.append("sh")
        arg_list.append("-c")

    arg_list.append("echo " + param)

    pb = os.popen(' '.join(arg_list))

    try:
        output = pb.read()
        response.set_data(output)
        return response
    except Exception as e:
        print("Problem executing command - Test Case")
        raise RuntimeError(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
