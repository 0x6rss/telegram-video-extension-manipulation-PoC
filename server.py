# for ip logger scenario (optional)

from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from werkzeug.serving import make_server

app = Flask(__name__)
app.config['DEBUG'] = False

CORS(app)  

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/log_ip', methods=['POST'])
def log_ip():
    try:
        data = request.json  
        if not data:
            return jsonify({"error": "No data received"}), 400

        ip_address = data.get('ip')
        country = data.get('country')
        region = data.get('region')
        city = data.get('city')
        isp = data.get('isp')

        if ip_address:
            log_entry = f"IP: {ip_address} | Country: {country} | Region: {region} | City: {city} | ISP: {isp}\n"


            with open("ip_log.txt", "a") as file:
                file.write(log_entry)

            print("Logged:", log_entry)  

            return jsonify({"message": "IP logged"}), 200

        return jsonify({"error": "Invalid data format"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
