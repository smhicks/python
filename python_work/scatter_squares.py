import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

#x_values = [1,2,3,4,5]
#y_values = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color='red', s=10)

ax.set_title("Caity's Stress", fontsize=24)
ax.set_ylabel('Days', fontsize=14)
ax.set_xlabel('Number of Meetings with Shawn', fontsize=14)

ax.tick_params(labelsize=14)

ax.axis([0, 1100, 0, 1_100_000])

ax.ticklabel_format(style='plain')

#plt.savefig('steve_plot.png', bbox_inches='tight')

plt.show()