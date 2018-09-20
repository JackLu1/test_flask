from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	image = "<a href='https://www.ubuntu.com/'><img src='./static/ubuntu.png'></a>"
	return '<a href="./static/test.html">ddd</a> <br>' + image

if __name__ == "__main__":
	app.debug = True
	app.run()
