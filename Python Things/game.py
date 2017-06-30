start = '''
You're walking home, you're tired, a friend has told you of a shortcut home.
Do you take this shortcut or not?
'''
take_shortcut = '''
You feel something cold on your shoulder.
Do you look at your shoulder?
'''
no_shortcut = '''
You continue walking.
You continue walking.
'''
jacket = '''
All of a sudden you feel something cold on yout shoulder. it turns out to be bird poo.
Do you take off your jacket? Or do you leave it on?
'''
take_off_jacket = '''
You take off your jacket and it begins to rain. You begin to run home.
You wake up in your bed at home. It was all a dream.
'''
keep_on_jacket = '''
You continue to walk home. Flies swarm you, yet you make it.
You wake up in your bed at home. It was all a dream.
'''
you_look = '''
You see a hand on your shoulder.
'''
you_dont_look = '''
You continue walking witha dreadful feeling in your stomach, and chills in your
spine. Until you come across a homeless man. He asks you for money.
Do you give him money?
'''
give_him_money = '''
He leaves you alone.
You wake up at home and it was all a dream.
'''
you_ignore_him = '''
Suddenly there's a bright light. The man is no longer homeless. Light is glowing
around him and he is now floating with wings. He curses you for your cruelty and
curses you. You black out...
'''
you_wake_up = '''
You wake up in a unknown placed tied to a bed.
Do you struggle or stay still?
'''
bed_struggle = '''
As you begin to struggle a poison begins to fufill the room, and you begin to suffocate.
Do you let yourself pass out or do you hold your breath?
'''
hold_your_breath = '''
The posion clears the room and a man with a surgical mask on enters the room with a set of surgical instruments.
Do you scream or try to run?
'''
let_go = '''
You let go of your breath and give up.
You suddenly wake up in your room to discover that the entire affair was all a dream.
'''
try_to_run = '''
You leap off the bed and try to run out of the room. The man signals to a seeming
no one and people with cream-coloured buglar mask like socks, tied at the top
enter the room. They're dressed only in hospital robes and wear latex gloves. In
one of their hands they hold a IV. They push you to the bed and you black out...
'''
metal_suit = '''
You wake up inside a metal suit. All pain you felt earlier you now, do not feel.
People in front of you scream. You feel no empathy.
You. Feel. Nothing.
Suddenly you jolt awake. You're in your room and you've just woken up.
It was all a dream...
'''
stay_still = '''
a man walks into the room. he has no face. he unties you from the bed.
Do you stay on the bed or move to hide under the bed?
'''
scream = '''
a hand collapses over your mouth and you pass out...
'''
bed_struggle = '''
You begin to suffocate as a poison enters the room.
Do you hold your breath or let go?
'''
hide = '''
You scuttle to hide under the bed, and suddenly it sags down. You come out to
check who is on top of the bed, but no one if there. You then hear a rustling
under the bed. You peek down and there's, once more, nothing there. Hand collapse
around your neck and you are strangled to death...
You wake up in your room at home. It was all a dream.
'''
run = '''
You begin to run as fast as you can and you hear heavy footsteps behind you. You
turn away around and nothing's there, so you turn back around again. You continue
to run, and until you feel a hand on your shoulder again. Everything goes black...
'''

print(start)

print("if you take the shortcut type 'take shortcut' if you don't, type 'take normal way home'")

user_input = input()
if user_input == "take shortcut":
    print(take_shortcut)
    print("if you look type 'look' if you don't, type 'don't look'")
    user_input = input()
    if user_input == "look":
        print(you_look)

        print("if you scream type 'scream' if run type 'run'")
        user_input = input()
        if user_input == "scream":
            print(scream)
            print(you_wake_up)

        elif user_input == "run":
            print(run)
            print(you_wake_up)

            print("if you struggle type 'struggle' if you don't type 'stay still'")
            user_input = input()
            if user_input ==




print("if you hide under the bed type 'hide' if you stay on the bed type 'stay'")
user_input = input()
if user_input == "stay":
    print(bed_stay)

    print("if you don't your breath type 'hold' if you don't, type 'let go'")
    user_input = input()
    if user_input == "hold":
        print(hold_your_breath)

        print("if you try to run type 'run' if you don't type 'be still'")
        user_input = input()
        if user_input == "run":
            print(try_to_run)
            print(metal_suit)

        elif user_input == "stay still":
            print(stay_still)

    elif user_input == "let go":
        print(let_go)

elif user_input == "hide":
    print(hide)
    




    elif user_input == "don't look":
        print(you_dont_look)

        print("if you give him money type 'yes' if you don't, type 'no'")
        user_input = input()
        if user_input == "no":
            print(you_ignore_him)
            print(you_wake_up)

            print("if you struggle type 'struggle' if you don't type 'stay still'")
            user_input = input()
            if user_input == "struggle":
                print(bed_struggle)

                print("if you don't your breath type 'hold' if you don't, type 'let go'")
                user_input = input()
                if user_input == "hold":
                    print(hold_your_breath)

                    print("if you try to run type 'run' if you don't type 'be still'")
                    user_input = input()
                    if user_input == "run":
                        print(try_to_run)
                        print(metal_suit)

                    elif user_input == "stay still":
                        print(stay_still)

                elif user_input == "let go":
                    print(let_go)

            elif user_input == "stay still":
                print(stay_still)

        elif user_input == "no":
            print(give_him_money)

elif user_input == "take normal way home":
    print(no_shortcut)
    print(jacket)
    print("if you take off your jacket type 'take off jacket' if you don't, type 'keep jacket on'")

    user_input = input()
    if user_input == "take off jacket":
        print(take_off_jacket)

    elif user_input == "keep jacket on":
        print(keep_on_jacket)
