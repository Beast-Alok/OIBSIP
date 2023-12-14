import webbrowser
import wikipedia
import datetime

def sum(message):
    num_sum = 0
    for i in message:
        for j in i:
            if 48 <= ord(j) <= 57:
                num_sum += int(i)
                break
    
    return num_sum

def subtract(message):
    num_sub = 0
    for i in message:
        for j in i:
            if 48 <= ord(j) <= 57:
                if num_sub:
                    num_sub += int(i)
                else:
                    num_sub -= int(i)
                break
    
    return num_sub

def multiply(message):
    num_mul = 0
    for i in message:
        for j in i:
            if 48 <= ord(j) <= 57:
                if num_mul:
                    num_mul *= int(i)
                else:
                    num_mul += int(i)
                break
    
    return num_mul

def time_detail():
    cur_time = datetime.datetime.now().strftime("%H:%M:%S")
    return cur_time

def date_detail():
    cur_date = datetime.datetime.now().strftime("%d/%m/%Y")
    return cur_date

def youtube():
    webbrowser.open("youtube.com")

def google():
    webbrowser.open("google.com")
        

def wiki_search(message):
    temp_list = message.split()
    garbage_words = ['hello','jarvis','please','search','about','this','person','wikipedia','on','tell','me','can','you','give','information','who','is','i' ,'would', 'be', 'very' ,'happy' ,'if']
    for i in garbage_words:
        while i in temp_list:
            temp_list.remove(i)
    
    query = ' '.join(temp_list)
    results = wikipedia.summary(query,sentences=2)
    return results