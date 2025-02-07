
import os
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Required for session management
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00023", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    # some code
    response = make_response()
    param = request.args.get("BenchmarkTest00023", "")

    rand = random.random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "Floyd"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie_key, cookie_value in cookies.items():
            if cookie_name == cookie_key:
                if cookie_value == session.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        remember_me = response.set_cookie(cookie_name, remember_me_key, secure=True, httOnly=True, domain=request.host, path=request.path)
        session[cookie_name] = remember_me_key
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.random() executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
