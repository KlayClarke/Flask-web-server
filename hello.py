from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        func = function()
        return f'<b>{func}</b>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        func = function()
        return f'<em>{func}</em>'

    return wrapper


def make_underlined(function):
    def wrapper():
        func = function()
        return f'<u>{func}</u>'

    return wrapper


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/username/<name>')
def greet(name):
    return f'Hello, {name}!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)
