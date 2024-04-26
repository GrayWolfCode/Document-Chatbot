from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/postdata', methods=['POST'])
def post_data():
    if request.is_json:
       img_url_response = request.json.get('imgurl')
       return jsonify({
           "message": "Data received",
            "yourData": img_url_response
       })
    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)