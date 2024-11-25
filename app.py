import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    # Få argumentene fra OpenAI
    data = request.json
    location = data.get("location", "Stavanger")

    # Kall Railway API
    railway_url = f"https://courageous-quietude-production.up.railway.app/api/weather?location={location}"
    response = requests.get(railway_url)
    weather_data = response.json()

    # Returner værdataene til OpenAI
    return jsonify({
        "temperature": weather_data["temperature"],
        "condition": weather_data["condition"],
        "wind_speed": weather_data["details"]["wind_speed"],
        "wind_direction": weather_data["details"]["wind_direction"],
        "humidity": weather_data["details"]["humidity"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
