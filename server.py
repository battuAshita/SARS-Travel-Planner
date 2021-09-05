from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# Hit the api to find the information about a specific country
def getInfo(name):
    final_result = list()
    country = name
    URL = 'https://www.worldometers.info/coronavirus/country/{}/'.format(country)
    response = requests.get(URL)
    if response.status_code == 200:
        parse_content = BeautifulSoup(response.content, 'html.parser')
        result = parse_content.find_all('div', class_='maincounter-number')

        for key in result:
            final_result.append(key.find('span').text)

    else:
        final_result.append('No result')

    return final_result


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/info', methods=['POST'])
def displayInfo():
    if request.method == 'POST':
        country = request.form['country_name']

        try:
            response = getInfo(country)
            return render_template('info.html', response=response)
        except LookupError:
            response = ['Data not available', 'Data not available', 'Data not available']
            print(response)
            return render_template('info.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
