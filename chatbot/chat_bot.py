import re
import main
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommands(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said : {query}\n")

    except Exception as e:
        return "Query not recognized by the bot"
    return query


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainity += 1
    
    # Calculates the percentage of recognised words in a user messages
    percentage = float(message_certainity) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    

    #examples prompt for AI
    response('Sir, I don\'t have any knowledege regarding this prompt!',[""], single_response=True)
    response('Hello sir!',['hello', 'hi', 'hey'], single_response=True)
    
    response('I am doing fine sir, and whats about you?',['how', 'are', 'you', 'doing'], required_words=['how','you','doing'])
    response('Thank you very much sir !',['i', 'love', 'jarvis'], required_words=['love','jarvis'])
    response('Thank you sir!',['i', 'great', 'jarvis'], required_words=['great','jarvis'])
    response('Thank you sir!',['very', 'good', 'jarvis'], required_words=['good'])
    
    response('Opening youtube sir!',['can', 'open', 'visit', 'youtube'], required_words=['youtube'])
    response('Opening google sir!',['can', 'open', 'visit', 'google'], required_words=['google'])

    response(f'Sir, sum of given number is {main.sum(message)}',['what', 'answer', 'sum' , 'and'], required_words=['sum'])
    response(f'Sir, addition of given number is {main.sum(message)}',['add', 'answer', 'sum', 'and' ], required_words=['add'])
    response(f'Sir, addition of given number is {main.sum(message)}',['addition', 'answer', 'sum', 'and' ], required_words=['addition'])
    
    response(f'Sir, if we subtract given number then our answer is {main.subtract(message)}',['what', 'answer','from', 'subtract'], required_words=['subtract'])
    response(f'Sir, subtraction of given number is {main.subtract(message)}',['what', 'answer','from', 'subtraction'], required_words=['subtraction'])
    
    response(f'Sir, if we multiply given number then answer is {main.multiply(message)}',['what', 'answer', 'multiply'], required_words=['multiply'])
    response(f'Sir, multiplication of given number is {main.multiply(message)}',['what', 'answer', 'multiplication'], required_words=['multiplication'])
    
    response('Sir, the currrent time is ',['what', 'time', 'current'], required_words=['time'])
    response('Sir, the today\'s date is ',['what', 'date', 'today\'s'], required_words=['date'])
    response('wikipedia',['search', 'wikipedia', 'about','person','tell','information','who'], single_response=True)
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,:!.-]\s*', user_input.lower())
    # print(split_message)
    response = check_all_messages(split_message)
    return response


if __name__ == "__main__":
    print("Bot: Hello Sir, this is your personal ai assistant. What can i help you?")
    speak("Hello Sir, this is your personal ai assistant. What can i help you?")
    while True:
        message = takeCommands().lower()
        if("quit" in message):
            print("Bot: Have a nice day sir!")
            speak("Have a nice day sir!")
            break
        elif(message == "query not recognized by the bot"):
            print("Bot: I didn\'t get what you said, please say again\n")
            speak("I didn\'t get what you said, please say again")
            continue
        else:
            print(f"You: {message}")
            bot_response = get_response(message)
            if "time" in bot_response:
                bot_response += main.time_detail()
            elif "date" in bot_response:
                bot_response += main.date_detail()
            elif 'wikipedia' in bot_response:
                try:
                    bot_response = "Sir, According to wikipedia " + main.wiki_search(message)
                except Exception as e:
                    bot_response = "Sir, unable to search right now or you have searched something wrong!"

            print('Bot: ' + bot_response,'\n')
            speak(bot_response)
            
            #other functionalities
            if "youtube" in  bot_response:
                main.youtube()
            elif "google" in  bot_response:
                main.google()