from flask import Flask,render_template,request                 //importing the flask class from Flask.
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__) 
corona_bot = ChatBot('CoronaBot',storage_adapter='chatterbot.storage.SQLStorageAdapter',
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

trainer = ChatterBotCorpusTrainer(corona_bot) # training the chabot with help of chatterbot corpus.
 # this is the data set which it is get trainig
trainer.train("data/Corona_data.yml")
trainer.train("data/Personal_question.yml")

@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(corona_bot.get_response(userText))


if __name__ == "__main__":
     app.run(debug = True)


