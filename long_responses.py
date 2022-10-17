from http.client import responses
import random

R_EATING = "I don't eat. Bro, I am a bot"

def unknown():
    response = ['Could you please rephrase  that?',"...","Sounds about right","What does that mean?"][random.randrange(4)]

    return response
