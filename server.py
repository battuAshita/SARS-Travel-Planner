from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

# Creating ChatBot Instance
chatbot = ChatBot(
    'SARSBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training a bot
data_quesans = open('train_it/quesans.txt').read().splitlines()
data_personal = open('train_it/personal.txt').read().splitlines()

training_data = data_quesans + data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)


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
            recovered = int(re.sub('[,]', '', response[2]))
            active = int(re.sub('[,]', '', response[0]))
            deaths = int(re.sub('[,]', '', response[1]))
            safety = 1
            print(safety)
            if safety >= 90:
                colour = 'green'

            elif 50 <= safety < 90:
                colour = 'yellow'

            elif safety < 50:
                colour = 'red'

            return render_template('info.html', response=response, colour=colour)
        except LookupError:
            response = ['Data not available', 'Data not available', 'Data not available']
            print(response)
            return render_template('info.html', response=response, colour=colour)


@app.route('/botPage', methods=['GET'])
def get_bot_page():
    if request.method == 'GET':
        return render_template("bot.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == '__main__':
    app.run(debug=True)
