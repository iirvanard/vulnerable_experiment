
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00004", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("trustbound-00/BenchmarkTest00004.html"))
        user_cookie = make_response("Set-Cookie: BenchmarkTest00004=color; Max-Age=180; Secure; Path=" + request.path + "; Domain=" + request.host)
        response.headers.add('Set-Cookie', user_cookie)
        return response
    else:
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if the_cookies:
            if 'BenchmarkTest00004' in the_cookies:
                param = urllib.parse.unquote(the_cookies['BenchmarkTest00004'])

        request.environ['session'][param] = "10340"
        return f"Item: '{param}' with value: '10340' saved in session."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
