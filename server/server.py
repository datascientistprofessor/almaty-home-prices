from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    room = int(request.form['room'])
    sq_m = float(request.form['sq_m'])
    floor = int(request.form['floor'])
    year = int(request.form['year'])
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(room,sq_m,floor,year,location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()