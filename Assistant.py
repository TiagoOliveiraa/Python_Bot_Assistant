import telebot
#import keys

API_KEY = "5626356982:AAGPdI_laczEEHUzloleQ27KcKgD3akJa8Y"

bot = telebot.TeleBot(API_KEY)

#megane_seguro =

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

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["help"])
def help(message):
    text = """
    Comandos:
    
        /help - Lista de Comandos
        /carro - Comandos do Carro        
Clicar numa das opções acima"""

    bot.reply_to(message, text)

@bot.message_handler(commands=["carro"])
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

def verify(message):
    return True

@bot.message_handler(func=verify)
def answer(message):
    bot.reply_to(message, "Não conheço esse comando:\n\n /help para comandos")


bot.polling()

