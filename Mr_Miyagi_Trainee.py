# mr Miyagi trainee project
# Ask for user input and depending on the response, mr Miyagi will respond.
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
# every time you ask a question --> Mr. Miyagi responde with
# --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
# --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
# --> 'Remeber, best block, not to be there..'
# anything else you say:
# --> 'do not lose focus. Wax on. Wax off.ake it so you keep playing until we say: 'Sensei, I am at peace'
# --> 'Sometimes, what heart know, head forget'

talk_to_sensei = 'yes'


while talk_to_sensei.replace(' ', '').lower() != 'sensei,iamatpeace':


    user_input = input('Hello young grasshopper, tell me what is on your mind: ').strip().lower()

    if 'sensei' != user_input[:6]:
        print('You are smart, but not wise - address me as Sensei please')
        talk_to_sensei = input('If you no-longer want to talk to Mr Miyagi, say: Sensei, I am at peace : ')

    elif 'block' in user_input or 'blocking' in user_input:
        print('Remember, best block, not to be there..')
        talk_to_sensei = input('If you no-longer want to talk to Mr Miyagi, say: Sensei, I am at peace : ')

    elif '?' in user_input or 'how' in user_input or 'what' in user_input or 'do' in user_input:
        print('Questions are wise, but for now. Wax on, and Wax off!')
        talk_to_sensei = input('If you no-longer want to talk to Mr Miyagi, say: Sensei, I am at peace : ')

    else:
        print("do not lose focus. Wax on. Wax off")
        talk_to_sensei = input('If you no-longer want to talk to Mr Miyagi, say: Sensei, I am at peace : ')

print(talk_to_sensei.replace(' ', '').lower() )
