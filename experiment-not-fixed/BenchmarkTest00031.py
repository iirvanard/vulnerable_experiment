
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00031", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request()
    return handle_request()

def handle_request():
    response = ""
    param = ""
    map_values = request.args.to_dict()

    if map_values:
        values = map_values.get("BenchmarkTest00031")
        if values:
            param = values

    request.environ['werkzeug.session'].update({'userid': param})

    response += f"Item: 'userid' with value: '{encode_for_html(param)}' saved in session."
    return response

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
