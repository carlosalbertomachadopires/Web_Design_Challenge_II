from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/cloudiness")
def clou():
    return render_template("Lat_vs_Clou.html")

@app.route("/humidity")
def humi():
    return render_template("Lat_vs_Humi.html")

@app.route("/temperature")
def temp():
    return render_template("Lat_vs_Temp.html")

@app.route("/wind")
def wind():
    return render_template("Lat_vs_Wind.html")

@app.route("/comparisons")
def compa():
    return render_template("Comparisons.html")

if __name__ == "__main__":
    app.run(debug=True)
