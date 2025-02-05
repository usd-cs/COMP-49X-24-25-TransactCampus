from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """
    Renders the homepage/dashboard.

    This function handles requests to the root URL ("/")
    and returns the rendered "index.html" template. Containing the dashboard
    to look at student breakfast dining metrics from a report generated
    in PowerBi.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
