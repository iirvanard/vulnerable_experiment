
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00032", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')
    map = request.form

    param = ""
    if map:
        values = map.getlist("BenchmarkTest00032")
        if values:
            param = values[0]

    try:
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{param}'"

        # Simulate the execution of the SQL statement
        # org.owasp.benchmark.helpers.DatabaseHelper.JDBCtemplate.execute(sql)

        response.set_data(
            "No results can be displayed for query: "
            + sql.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            + "<br>"
            + " because the Spring execute method doesn't return results."
        )
    except Exception as e:
        # Simulate handling of SQL errors
        response.set_data("Error processing request.")

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
