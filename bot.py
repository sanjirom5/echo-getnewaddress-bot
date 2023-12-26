import config
import telebot
from bitcoinrpc.authproxy import AuthServiceProxy

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    rpc = AuthServiceProxy("http://{user}:{passwd}@{host}:{port}".format(user="kzcashrpc", passwd="Svt6sBYAUSsA2bTAkux8Fk3H", host="localhost", port="8276"))
    if message.text == "getnewaddress": bot.send_message(message.chat.id, rpc.getnewaddress())
    else: bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
