from flask import Flask, request, jsonify
from hescorehpxml import main
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:4999"], 
     methods=["POST"])

@app.route('/', methods=['POST'])
def handle_data():
    req = request.get_json()    
    decoded_content = base64.b64decode(req['hpxmlBase64String'])
    with open("input.xml", "wb") as file:
        file.write(decoded_content)
    print("XML file has been saved as 'input.xml'")
    res = main(["input.xml"]) 
    print("res is ",res)
    return jsonify(res) 

if __name__ == '__main__':
    app.run(debug=True, port=5002)

