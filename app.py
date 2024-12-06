from flask import Flask, jsonify, render_template
from pb_api import get_embed_token


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/embed-info", methods=["GET"])
def get_embed_info():
    try:
        embed_token = get_embed_token()
        return jsonify(embed_token)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


"""@app.route("/data", methods=["GET"])
def get_data():
    query = "SELECT * FROM your_table"
    with engine.connect() as connection:
        result = connection.execute(query)
        data = [dict(row) for row in result]
    return jsonify(data)"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
