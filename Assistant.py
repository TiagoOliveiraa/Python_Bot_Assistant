import telebot
from apscheduler.schedulers.background import BackgroundScheduler
import cars
#from datetime import datetime
from task import *
import time


API_KEY = "5626356982:AAGPdI_laczEEHUzloleQ27KcKgD3akJa8Y"
TiagoID = 1374815440

bot = telebot.TeleBot(API_KEY)


lista_tarefas = []


def TesteDiario():

    cars.check_dates(bot,TiagoID)

scheduler = BackgroundScheduler()
scheduler.add_job(TesteDiario,'cron',hour = 11)
scheduler.start()



@bot.message_handler(commands=["megane"])
def megane(message):
    
    if "seguro" in message.text:
        cars.change_seguro(bot,message)
    if "insp" in message.text:
        cars.change_inspecao(bot,message)
    if "oleo" in message.text:
        cars.change_oleo(bot,message)
    cars.megane(bot,message)

@bot.message_handler(commands=["laguna"])
def laguna(message):
    if "seguro" in message.text:
        cars.change_seguro(bot,message)
    if "insp" in message.text:
        cars.change_inspecao(bot,message)
    if "oleo" in message.text:
        cars.change_oleo(bot,message)

    cars.laguna(bot,message)

@bot.message_handler(commands=["clio"])
def clio(message):
    if "seguro" in message.text:
        cars.change_seguro(bot,message)
    if "insp" in message.text:
        cars.change_inspecao(bot,message)
    if "oleo" in message.text:
        cars.change_oleo(bot,message)

    cars.clio(bot,message)

@bot.message_handler(commands=["expert"])
def expert(message):
    if "seguro" in message.text:
        cars.change_seguro(bot,message)
    if "insp" in message.text:
        cars.change_inspecao(bot,message)
    if "oleo" in message.text:
        cars.change_oleo(bot,message)

    cars.expert(bot,message)

@bot.message_handler(commands=["help"])
def help(message):
    text = """
    Comandos:
    
        /help - Lista de Comandos
        /cars - Comandos de carros        
        /task - Lista de tarefas
Clicar numa das opções acima
        """

    bot.reply_to(message, text)

@bot.message_handler(commands=["cars"])
def carro(message):
    text = """
    Carros disponiveis:
        Renault:
            /megane
            /laguna
            /clio
        Peugeot:
            /expert
    """


    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["task"])
def tasks(message):

    if "add" in message.text:
        task_add(message,bot)

    elif "clear" in message.text:
        task_clear(message,bot,lista_tarefas)

    elif "list" in message.text:
        task_list(message,bot)
    
    elif "del" in message.text:
        task_del(message,bot) 
       
    else:
        task_general(message,bot)


def verify(message):
    return True

@bot.message_handler(func=verify)
def answer(message):
    bot.reply_to(message, f"Não conheço esse comando:\n\n /help para comandos")

bot.polling()

