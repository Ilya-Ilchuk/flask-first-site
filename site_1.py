# app.py
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


menu = ['Параметри', 'Щось там щось там щось там', 'Перемога']
numbers = range(0, 100)


@app.route("/")
def index():
    return render_template('index.html', title="About Flask", menu=menu, numbers=numbers)


if __name__ == "__main__":
    app.run(debug=True)
