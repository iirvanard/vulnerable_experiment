
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00007", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    if request.headers.get("BenchmarkTest00007") is not None:
        param = request.headers.get("BenchmarkTest00007")

    param = param  # URL Decode not needed as Flask handles this automatically

    cmd = "some_command_here"  # Replace with appropriate command
    args = [cmd]
    args_env = [param]

    try:
        process = os.popen(' '.join(args))  # Using os.popen to execute command
        output = process.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(e)
        return response

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
