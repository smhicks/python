"""Printing Dictonary"""
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(alien_0)
print(f"Orignal Position: {alien_0["x_position"]}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New Position: {alien_0['x_position']}")


del alien_0['speed']
print(alien_0)


