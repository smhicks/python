import plotly.express as px
from die import Die


die1 = Die()
die2 = Die()

results = []

for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []

max_result = die1.num_sdies + die2.num_sdies
poss_results = range(2, max_result+1)
for value in poss_results:
    frequncy = results.count(value)
    frequencies.append(frequncy)

#print(frequencies)
#visualize the results
TITLE = "Results of rolling one D6 1,000 times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=TITLE, labels = labels)

fig.update_layout(xaxis_dtick=1)

fig.show()
