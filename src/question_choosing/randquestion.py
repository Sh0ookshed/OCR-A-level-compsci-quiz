#This function chooses a random question from the question bank.

#libraries
import random

def random_question_chooser(qlist):
    
    topic_choice = qlist[random.randint(0,len(qlist)-1)]

    question_choice = topic_choice[random.randint(0,len(topic_choice)-1)]
    
    return(question_choice)