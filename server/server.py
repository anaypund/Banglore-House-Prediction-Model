from flask import render_template, Flask, request, jsonify
import util

app = Flask(__name__)



@app.route('/get-location-name', methods = ['GET'])
def get_location_name():
    response = jsonify({
        'location' : util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict-home-price', methods = ['GET', 'POST'])
def predict_home_price():
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']
    total_sqft = request.form['total_sqft']
    response = jsonify({
        'estimated_price' : util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    return response
    

if __name__ == '__main__':
    util.load_saved_artifacts()
    app.debug = True
    app.run()
    print("python server is running")