from flask import Flask

from olympics.models import app_config, Olympics


app = Flask(__name__)
app.config.update(app_config)

olympics = Olympics()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/medals')
def get_medals():
    return olympics.get_medals()

@app.route('/medals/<country>')
def get_medals_by_country(country):
    pass


if __name__ == '__main__':
    app.run()
