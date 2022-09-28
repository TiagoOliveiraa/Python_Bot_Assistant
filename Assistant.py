import telebot
import time
from apscheduler.schedulers.background import BackgroundScheduler
#import keys

API_KEY = "5626356982:AAGPdI_laczEEHUzloleQ27KcKgD3akJa8Y"

bot = telebot.TeleBot(API_KEY)

lista_tarefas = []

#megane_seguro =

def print_teste():

    bot.send_message("Isto é uma mensagem de teste")


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
        /tasks - Lista de tarefas
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
        lista_texto = message.text.split()
        lista_texto.remove("/task")
        lista_texto.remove("add")
        texto = ''.join(map(str, lista_texto))

        file = open('tasks.txt','a+')
        file.write("%s\n" % texto)
        file.close()

        bot.reply_to(message, f"Adicionada a tarefa: {texto}")

    elif "clear" in message.text:
        file = open('tasks.txt','a+')
        file.truncate(0)
        lista_tarefas.clear()

        bot.send_message(message.chat.id, "Lista de tarefas limpa com sucesso!")

    elif "list" in message.text:

        file = open('tasks.txt','r+')
        for line in file:
            line = line.strip()
            lista_tarefas.append(line)
        file.close()

        text = "Lista de tarefas:"
        for i in lista_tarefas:
            text = text + '\n'
            text = text + str(i)

        bot.send_message(message.chat.id, text)

    else:

        general_text = """
        Comandos Task:
/task add «Texto» >Adiciona tarefa
/task clear >Limpa lista de tarefas
/task list >Lista de tarefas
        """

        bot.reply_to(message, general_text)


def verify(message):
    return True

@bot.message_handler(func=verify)
def answer(message):
    bot.reply_to(message, "Não conheço esse comando:\n\n /help para comandos")


bot.polling()

