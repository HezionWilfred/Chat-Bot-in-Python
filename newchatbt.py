from chatterbot import ChatBot
import collections.abc
import time
from chatterbot.trainers import ListTrainer
if not hasattr(time, 'clock'):
    time.clock = time.perf_counter
collections.Hashable = collections.abc.Hashable
# Create object of ChatBot class
bot = ChatBot('Buddy')
# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
    'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='https://genius.com/',
    logic_adapters = [  
      'chatterbot.logic.MathematicalEvaluation',  
      'chatterbot.logic.BestMatch'  
      ]  
)

trainer = ListTrainer(bot)
trainer.train([
'Hi',
"please send me the referal code",
'Hello',
'May i help',
'welcome users',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!',
'Thanks'
])

# Get a response to the input text 'I would like to book a flight.'
response = bot.get_response('I have a complaint.')

print("Bot Response:", response)
name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)