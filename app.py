from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello Flask'


@app.route('/user/<name>')
def user_page(name):
    return f'User:{name}'


@app.route('/test')
def test_url_for():
    print(url_for('hello_world'))
    print(url_for('user_page', name='zhangsan'))
    print(url_for('user_page', name='lisi'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'


if __name__ == '__main__':
    app.run()
