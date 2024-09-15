alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':7}
alien_2 = {'color':'red', 'points':9}
alien_3 = {'color':'blue', 'points':3}

aliens = [alien_0, alien_1, alien_2, alien_3]

#print(aliens)

#for alien in aliens:
    #print(alien)


aliens = []
point_value = 5
for alien_number in range(30):
    new_alien = {'color':'green', 'points':{point_value}, 'speed':'slow'}
    aliens.append(new_alien)
    point_value = point_value + 2

for alien in aliens:
    print(alien)
print(len(aliens))