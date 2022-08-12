from matplotlib import pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']
# Label each point
plt.scatter(friends,minutes)
for label, friend_count, minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
        # label next to the point
        xy=(friend_count,minute_count),
        xytext=(5,-5),
        textcoords='offset points'
        )

plt.title("Minutes par jour / Nombre d'amis")
plt.xlabel("Nombre d'amis")
plt.ylabel("Temps quotidien sur le site (min)")
plt.show()
    
