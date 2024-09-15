bicycles = ['trek', 'salsa', 'surly', 'cannondale', 'specialized']



message = f'My first bike was a {bicycles[1].title()}'
print(message)

motorcycles = ['honda','yamaha','KTM']
motos = motorcycles[2]

print(motos)

motorcycles[0] = 'husky'

motos = motorcycles[0]

print(motos)

motorcycles.append('Suzuki')
print(motorcycles[-1])