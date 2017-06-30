from random import *

three_list = ["it will hurt", "i was death", "dear cammy", "i just can't", "not anymore", "where are you?", "welcome death", "we were art", "i'll miss you", "to the sky", "one more breath", "s" "idiot"]
five_list = ["bleaker than the grey", "smiling burns my face","can't control the change", "are you joshing me?", "rally the people", "i wish for a chance", "i'm an alien", "love you forever", "fear is in her eyes", "words are weapons", "i don't give a fuck", "to those that hate us", "you motherfuckers","please do mind the gap", "and with a clap, death"]

#Generates a random integer.
x = randint(0, len(five_list)-1)
y = randint(0, len(three_list)-1)
z = randint(0, len(three_list)-1)

print(three_list[y] + '\n' + five_list[x] + '\n' + three_list[z])
