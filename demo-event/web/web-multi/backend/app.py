
from flask import Flask

app = Flask(__name__)

@app.route('/secret')
def secret():
    return "1pc{multi_service_communication_is_working}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
