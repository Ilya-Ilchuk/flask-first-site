from flask import Flask, render_template


app = Flask(__name__)

menu = ['Параметри', 'Щось там щось там щось там', 'Перемога']


@app.route("/")
def index():
    return render_template('index.html', title="About Flask", menu=menu)


@app.route("/about")
def about():
    return "<h1>About</h1>"


if __name__ == "__main__":
    app.run(debug=True)
