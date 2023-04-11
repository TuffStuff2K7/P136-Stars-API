from Data import data
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"data": data,
                    "message": "Star Data API"}), 200

@app.route("/star")
def getPlanet():
    ind = request.args.get("index")
    star_data = next(i for i in data if i["Index"] == int(ind))
    return jsonify({"data": star_data, "message": "Success :)"}), 200

if(__name__ == "__main__"):
    app.run()
