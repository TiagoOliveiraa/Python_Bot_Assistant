from datetime import datetime as dt

def megane(bot,message):
    
    d = {}
    
    d["megane_seguro"] = 0
    d["megane_insp"] = 0
    d["megane_oleo"] = 0
    
    d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
    
    text = f"""
    Renault Megane 2001 1.9 dti 80 cv
    Condutor: Tiago Oliveira
    Matricula: 95-69-SA
    Seguro: {d["megane_seguro"]}
    Inspeção: {d["megane_insp"]}
    Óleo: {d["megane_oleo"]} km
    """

    bot.send_message(message.chat.id,text)
    
def laguna(bot,message):
    
    d = {}
    
    d["laguna_seguro"] = 0
    d["laguna_insp"] = 0
    d["laguna_oleo"] = 0
    
    d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
    
    text = f"""
    Renault Laguna 2011 1.5 dci 110 cv
    Condutor: Cláudia Oliveira
    Matricula: 17-19-UZ
    Seguro: {d["laguna_seguro"]}
    Inspeção: {d["laguna_insp"]}
    Óleo: {d["laguna_oleo"]} km
    """

    bot.send_message(message.chat.id, text)

def clio(bot,message):
    
    d = {}
    
    d["clio_seguro"] = 0
    d["clio_insp"] = 0
    d["clio_oleo"] = 0
    
    d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
    
    text = f"""
    Renault Clio 2003 1.5 dci 80 cv
    Condutor: Pedro Oliveira
    Matricula: 95-69-SA
    Seguro: {d["clio_seguro"]}
    Inspeção: {d["clio_insp"]}
    Óleo: {d["clio_oleo"]} km
    """

    bot.send_message(message.chat.id, text)
    
def expert(bot,message):
    
    d = {}
    
    d["expert_seguro"] = 0
    d["expert_insp"] = 0
    d["expert_oleo"] = 0    
    
    d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
    
    text = f"""
    Peugeot Expert 2000 2.0 hdi 100 cv
    Condutor: Pedro Oliveira
    Matricula: 12-43-TH
    Seguro: {d["expert_seguro"]}
    Inspeção: {d["expert_insp"]}
    Óleo: {d["expert_oleo"]} km
    """

    bot.send_message(message.chat.id, text)
    

def change_seguro(bot,message):
    if "/megane" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/megane")
        lista_texto.remove("seguro")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["megane_seguro"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data do seguro alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato de data inválido.")
            
    if "/laguna" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/laguna")
        lista_texto.remove("seguro")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["laguna_seguro"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data do seguro alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato de data inválido.")
            
    if "/clio" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/clio")
        lista_texto.remove("seguro")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["clio_seguro"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data do seguro alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato de data inválido.")
            
    if "/expert" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/expert")
        lista_texto.remove("seguro")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["expert_seguro"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data do seguro alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato de data inválido.")
        
def change_oleo(bot,message):
    if "/megane" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/megane")
        lista_texto.remove("oleo")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if data.isdigit():
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["megane_oleo"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Kilometros na ultima troca de oleo alterados.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
    if "/laguna" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/laguna")
        lista_texto.remove("oleo")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if data.isdigit():
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["laguna_oleo"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Kilometros na ultima troca de oleo alterados.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
    if "/clio" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/clio")
        lista_texto.remove("oleo")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if data.isdigit():
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["clio_oleo"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Kilometros na ultima troca de oleo alterados.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
    if "/expert" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/expert")
        lista_texto.remove("oleo")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if data.isdigit():
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["expert_oleo"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Kilometros na ultima troca de oleo alterados.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
def change_inspecao(bot,message):
    if "/megane" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/megane")
        lista_texto.remove("insp")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["megane_insp"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data da inspeção alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
    if "/laguna" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/laguna")
        lista_texto.remove("insp")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["laguna_insp"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data da inspeção alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
    if "/clio" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/clio")
        lista_texto.remove("insp")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["clio_insp"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data da inspeção alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")
            
    if "/expert" in message.text:
        lista_texto = message.text.split()
        lista_texto.remove("/expert")
        lista_texto.remove("insp")
        texto = ' '.join([str(i) for i in lista_texto])
        data = texto
        
        if dt.strptime(data, "%d/%m/%Y"):
            
        
            d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
            
            d["expert_insp"] = texto
                
            with open("car_values.txt","w+") as file:
                for key,value in d.items():
                    file.write("%s %s\n" % (key,value))
                    
            bot.send_message(message.chat.id, "Data da inspeção alterada.")
        
        else:
            
            bot.send_message(message.chat.id, "Formato inválido.")

def check_dates(bot,TiagoID):
    
    d = {line.split()[0] : line.split()[1] for line in open("car_values.txt")}
    
    for key,values in d.items():
        
        if key in ("megane_seguro","clio_seguro","laguna_seguro","expert_seguro","megane_insp","clio_insp","laguna_insp","expert_insp"):
            
            data = dt.strptime(values, "%d/%m/%Y").date()
            
            if data < dt.now().date():
                bot.send_message(TiagoID,f"{key} possui data desatualizada")
                
            delta = data - dt.now().date()
            
            if delta.days <= 30:
                bot.send_message(TiagoID,f"{key} a {delta.days} dias de terminar.")


