from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
     return '<h1 style="text-align:center">Hello!<h1>' \
            '<p>This is cat<p>' \
            '<img src="https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif"width=200>'

@app.route("/<name>")
def greet(name):
    return f"Hi {name}!"

if __name__ == "__main__":
    app.run(debug=True)