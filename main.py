import telebot
from telebot import types
import conf


bot = telebot.TeleBot(conf.API_token)

#name = ''
#number = 79999999999
#count = 0
value = []

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Информация")
    btn2 = types.KeyboardButton("Покупка")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, text="Привет, {0.first_name}! Здесь можно получить информацию по продукту [product_name], а так же выполнить его покупку".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Информация"):
        bot.send_message(message.from_user.id, text="[product_info]")
    elif(message.text == "Покупка"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton("Ф.И.О. получателя")
        #btn2 = types.KeyboardButton("Номер телефона получателя")
        #btn3 = types.KeyboardButton("Адрес пункта доставки СДЭК")
        #btn4 = types.KeyboardButton("Количество бутыльков")
        #back = types.KeyboardButton("Вернуться в главное меню")
        #markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.from_user.id, text="Пожалуйста, для заказа уточните следующую информацию:", reply_markup=markup)
        bot.send_message(message.from_user.id, "1. Ф.И.О. получателя")
        bot.register_next_step_handler(message, get_name)
    #elif (message.text == "Как меня зовут?"):
    #    bot.send_message(message.chat.id, "У меня нет имени..")

    #elif message.text == "Что я могу?":
    #    bot.send_message(message.chat.id, text="Поздороваться с читателями")

    #elif (message.text == "Вернуться в главное меню"):
    #    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #    button1 = types.KeyboardButton("👋 Поздороваться")
    #    button2 = types.KeyboardButton("❓ Задать вопрос")
    #    markup.add(button1, button2)
    #    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, text="Такой команды нет")


def get_name(message):
    name = message.text
    value.append(name)
    bot.send_message(message.from_user.id, "2. Номер телефона получателя")
    bot.register_next_step_handler(message, get_number)
    print(f'STEP 1 get_name\nUSER: {message.from_user.username}\nvalue = {value}')

def get_number(message):
    #bot.send_message(message.from_user.id, "2. Номер телефона получателя")
    number = message.text
    #while True:
    if len(str(number)) == 11 and str(number)[0] in ('7','8'):
        #break
        bot.send_message(message.from_user.id, "3. Адрес пункта доставки СДЭК")
        bot.register_next_step_handler(message, get_address)
        value.append(number)
    else:
        bot.send_message(message.from_user.id, 'Введите правильный номер')
        bot.register_next_step_handler(message, get_number)


    print(f'STEP 2 get_number\nUSER: {message.from_user.username}\nvalue = {value}')


def get_address(message):
    #bot.send_message(message.from_user.id, "3. Адрес пункта доставки СДЭК")
    address = message.text
    value.append(address)
    bot.send_message(message.from_user.id, "3. Введите необходимое количество [product_name]")
    bot.register_next_step_handler(message, get_count)
    print(f'STEP 3 get_address\nUSER: {message.from_user.username}\nvalue = {value}')

def get_count(message):
    #bot.send_message(message.from_user.id, "3. Введите необходимое количество [product_name]")
    #bot.send_message(message.from_user.id, "Почти закончили")
    count = message.text
    value.append(count)
    bot.register_next_step_handler(message, final_order)
    print(f'STEP 4 get_count\nUSER: {message.from_user.username}\nvalue = {value}')

def final_order(message):
    final_messege = f'''
    1: ФИО = {value[0]}\n
    2: Номер = {value[1]}\n
    3: Адрес = {value[2]}\n
    4: Кол-во = {value[3]}
    '''

    bot.send_message(message.from_user.id, f"Проверьте данные:\n{final_messege}")

bot.polling(none_stop=True)