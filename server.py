from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def map_func():
    return render_template('map.html')

def advice():
    return render_template('advice.html')


if __name__ == '__main__':
    app.run(debug=True)
