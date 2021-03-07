import telebot
import requests
from bs4 import BeautifulSoup as bs
import config

r = requests.get('https://sinoptik.ua/погода-душанбе')
html = bs(r.content, 'html.parser')
bot = telebot.TeleBot(config.token)

for el in html.select('#mainContentBlock'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    desc = el.select('.wDescription .description')[0].text

    print("Temperature minimum, " + t_min, "and maximum " + t_max + '\n' + desc)


@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, "Привет, погода на сегодня: \n"+ t_min + ', ' + t_max + '\n' + desc)


if __name__ == '__main__':
    bot.polling(none_stop=True)
