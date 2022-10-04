import telebot
from apscheduler.schedulers.background import BackgroundScheduler
#from datetime import datetime
from task import *
import time


API_KEY = "5626356982:AAGPdI_laczEEHUzloleQ27KcKgD3akJa8Y"
TiagoID = 1374815440

bot = telebot.TeleBot(API_KEY)


lista_tarefas = []

#megane_seguro =

def print_teste():

    bot.send_message(TiagoID,"Isto é uma mensagem de teste")

#scheduler = BackgroundScheduler()
#scheduler.add_job(print_teste,'interval',hours = 24)
#scheduler.start()


@bot.message_handler(commands=["megane"])
def megane(message):
    text = f"""
    Renault Megane 2001 1.9 dti 80 cv
    Condutor: Tiago Oliveira
    Matricula: 95-69-SA
    Seguro:
    Inspeção:
    Óleo: 
    """

    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=["laguna"])
def laguna(message):
    text = f"""
    Renault Laguna 2011 1.5 dci 110 cv
    Condutor: Cláudia Oliveira
    Matricula: 17-19-UZ
    Seguro:
    Inspeção:
    Óleo:
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["clio"])
def clio(message):
    text = f"""
    Renault Clio 2003 1.5 dci 80 cv
    Condutor: Pedro Oliveira
    Matricula: 95-69-SA
    Seguro:
    Inspeção:
    Óleo:
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["expert"])
def expert(message):
    text = f"""
    Peugeot Expert 2000 2.0 hdi 100 cv
    Condutor: Pedro Oliveira
    Matricula: 12-43-TH
    Seguro:
    Inspeção:
    Óleo:
    """

    bot.send_message(message.chat.id, text)

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

#bot.send_message(TiagoID,"Teste de entrada")

bot.polling()

