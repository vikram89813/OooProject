from flask import Flask, jsonify
import controller

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch():
    subject, fromId = controller.fetchMail()
    return jsonify({"subject": subject, "from": fromId})

if __name__ == '__main__':
    app.run(debug=True)