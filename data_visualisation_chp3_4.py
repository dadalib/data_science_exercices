from matplotlib import pyplot as plt

mentions = [500,505]
years = [2017,2018]

plt.bar(years, mentions,0.8)
plt.xticks(years)
plt.ylabel("Number nof labels terms 'data science'")

# Only plot in y after 500 technique to show fake grotthw
plt.axis([2016.5,2018.5,499,506])
# Plot everything
plt.axis([])
plt.title("Admirez cette hausse phénoménale")

plt.show()
