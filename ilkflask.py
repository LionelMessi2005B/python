from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Click here</a>"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)