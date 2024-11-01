from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get feature inputs from the form
        features = [
            float(request.form['length']),           # Length
            float(request.form['diameter']),         # Diameter
            float(request.form['height']),           # Height
            float(request.form['whole_weight']),     # Whole Weight
            float(request.form['shucked_weight']),   # Shucked Weight
            float(request.form['viscera_weight']),   # Viscera Weight
            float(request.form['shell_weight']),     # Shell Weight
            float(request.form.get('sex_f', 0)),     # Sex - Female
            float(request.form.get('sex_i', 0)),     # Sex - Indeterminate
            float(request.form.get('sex_m', 0)),     # Sex - Male
        ]

        # Create the payload
        payload = {
            "features": features
        }

        # Call the API
        api_url = "https://3utndsk058.execute-api.us-east-1.amazonaws.com/Dev/predictMlOps"
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            api_response = response.json()
            result = {
                "prediction": api_response.get("body"),
                "status_code": api_response.get("statusCode"),
            }
        else:
            result = {"error": response.status_code, "message": response.text}

    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Listen on all interfaces
#py