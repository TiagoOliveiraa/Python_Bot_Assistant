

def task_add(message,bot):

        lista_texto = message.text.split()
        lista_texto.remove("/task")
        lista_texto.remove("add")
        texto = ' '.join([str(i) for i in lista_texto])

        file = open('tasks.txt','a+')
        file.write("%s\n" % texto)
        file.close()

        bot.reply_to(message, f"Adicionada a tarefa: {texto}")


def task_clear(message,bot,lista_tarefas):
    with open('tasks.txt','a+') as file:
        file.truncate(0)
    lista_tarefas.clear()

    bot.send_message(message.chat.id, "Lista de tarefas limpa com sucesso!")

def task_list(message,bot):
    lista_tarefas = []    
    try:
        with open('tasks.txt','r+') as file:
            for line in file:
                line = line.strip()
                lista_tarefas.append(line)

        text = "Lista de tarefas:"
        for i in lista_tarefas:
            text = text + '\n'
            text = text + str(i)
    except:
        text = "Lista de tarefas vazia."

    bot.send_message(message.chat.id, text)

def task_general(message,bot):
    general_text = """
        Comandos Task:
/task add «Texto» >Adiciona tarefa
/task clear >Limpa lista de tarefas
/task list >Lista de tarefas
        """

    bot.reply_to(message, general_text)

def task_del(message,bot):
    
    lista_tarefas = []
    
    lista_texto = message.text.split()
    lista_texto.remove("/task")
    lista_texto.remove("del")
    texto = ' '.join([str(i) for i in lista_texto])
    
    try:
        with open('tasks.txt','r+') as file:
            for line in file:
                line = line.strip("\n")
                #if line not in lista_tarefas:
                lista_tarefas.append(line)
        
        if texto in lista_tarefas:
            lista_tarefas.remove(texto)
            with open('tasks.txt','w+') as file:
                file.truncate(0)
                file.seek(0)
                for i in lista_tarefas:
                    file.write("%s\n" % i)                    
            
            text = f"Task {texto} eliminada com Sucesso."
                    
            bot.send_message(message.chat.id, text)
            
        else:
            text = "Lamento, essa task não existe."
            bot.send_message(message.chat.id, text)

    except:
        text = "Lamento, essa task não existe."
        bot.send_message(message.chat.id, text)
    
    
    
    


