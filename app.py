from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from my Dockerized Flask Application!</h1><p>My first Cloud & DevOps project.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)