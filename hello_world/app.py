from flask import Flask
import os
import logging

app = Flask(__name__)

port = int(os.environ.get('PORT','5000'))
user = os.environ.get("CREATOR","app")

@app.route("/")
def hello():
    return "Hello World! My creator is {}".format(user)


if __name__ == '__main__':
    print("App is running on {}".format(port))
    app.run(debug=True, port=port,host="0.0.0.0")
