prompt = ("Tell me somethings and I'll repeat it")
prompt += ('\nEnter quit to end the program: ')

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)