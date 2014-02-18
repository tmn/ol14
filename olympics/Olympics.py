from flask import Flask

from olympics.models import Olympics, create_json_response

app = Flask(__name__)

olympics = Olympics()


@app.route('/')
def hello_world():
    return 'Wadup'

@app.route('/medals')
def get_medals():
    return create_json_response(olympics.get_medals())

@app.route('/medals/<country>')
def get_medals_by_country(country):
    res = olympics.get_medals_based_on_country(country)

    if len(res) == 0:
        return create_json_response([{"c":country, "t": 0}])
    else:
        return create_json_response(olympics.get_medals_based_on_country(country))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
