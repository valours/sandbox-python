from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Flask!'


# define main function call
if __name__ == '__main__':
    app.run(debug=True)
