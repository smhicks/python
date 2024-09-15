respnses = {}

polling_active = True
while polling_active:
    name = input('\nWhat is your name?: ')
    response = input('\nWhat mountian would you like to climb today?: ')

    respnses[name] = response

    repeat = input('\nAnyone else taking the poll? yes/no : ')
    if repeat == 'no':
        polling_active = False

print('\nPolling results: ')
for name, response in respnses.items():
    print(f'{name} would like to climb {response}')


