from flask import Flask, render_template, url_for

app = Flask(__name__)

# Power BI report URLs (replace with your actual values)
REPORT_URLS = {
    "overview": "https://app.powerbi.com/reportEmbed?reportId=d70721c9-b558-4a37-9bdc-f46ab94c3947&autoAuth=true&ctid=cec13ba4-cb08-43be-aed6-88c91cc16fcf",
    "nutrition": "https://app.powerbi.com/reportEmbed?reportId=4c934d8a-c8a5-4d42-8050-32353379315e&autoAuth=true&ctid=cec13ba4-cb08-43be-aed6-88c91cc16fcf",
    "groupings": "https://app.powerbi.com/reportEmbed?reportId=50711abe-7cee-4c7f-8de4-cb39eb1b6b81&autoAuth=true&ctid=cec13ba4-cb08-43be-aed6-88c91cc16fcf",
    "incentives": "https://app.powerbi.com/reportEmbed?reportId=55887605-607a-42f2-96df-ab55ccdaa697&autoAuth=true&ctid=cec13ba4-cb08-43be-aed6-88c91cc16fcf",
    "filter": "https://app.powerbi.com/reportEmbed?reportId=efb2d3f1-1a77-446f-adcf-b9fb04cd28a2&autoAuth=true&ctid=cec13ba4-cb08-43be-aed6-88c91cc16fcf",
}

@app.route("/")
def redirect_to_home():
    return home()

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/report/<report_id>")
def report(report_id):
    report_url = REPORT_URLS.get(report_id)
    if not report_url:
        return "Report not found", 404
    return render_template("report.html", report_url=report_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)