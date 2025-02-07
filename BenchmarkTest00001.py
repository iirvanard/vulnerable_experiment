import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00001", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00001.html"))
        
        # Set a cookie for the GET request
        user_cookie_value = 'FileName'  # You can replace this with actual data
        response.set_cookie(
    'BenchmarkTest00001', 
    user_cookie_value, 
    max_age=60*3,  # 3 minutes in seconds
    secure=True,  # Only send cookie over HTTPS
    httponly=True,  # Prevent JavaScript from accessing the cookie
    samesite='Strict',  # Restrict cookie to same-site requests
    path=request.path,  # Limit cookie to the current request path
    domain=request.host,  # Set domain to the request host (ensure this is correct and narrow)
)

        return response
    else:
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if 'BenchmarkTest00001' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00001'])

        file_name = None
        try:
            file_name = os.path.join('path/to/test/files', param)  # Adjust the path accordingly
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                return f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
        except Exception as e:
            print(f"Couldn't open FileInputStream on file: '{file_name}'")
            return f"Problem getting FileInputStream: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
