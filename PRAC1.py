import telepot
import datetime

token='1311310425:AAEx4ln4as6n5BWN1mGjMzZcaZvzCDMaRXY'
bot = telepot.Bot(token)
print (bot.getMe())

    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        if msg['text'].upper()=="DATE":
            bot.sendMessage(chat_id,str(datetime.datetime.today().strftime("%x")))
        else:
            bot.sendMessage(chat_id,"Commend for Date is:-Date")
bot.message_loop(handle)
