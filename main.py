#import required packages
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

#create chatbot
chatBot = ChatBot('Ethan')

trainer = ChatterBotCorpusTrainer(chatBot)
trainer.train("chatterbot.corpus.english")

#print(chatBot.get_response("Hello"))

print("Hi, I am Chatbot")
while True:
  query = input(">>>")
  print(chatBot.get_response(Statement(text = query, search_text = query)))
