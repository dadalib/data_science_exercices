from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100,49,41,40,40,40,40,40]
friend_counts = Counter(num_friends)
# The highest number is 100
xs = range(101)
ys= [friend_counts[x] for x in xs]

plt.bar(xs,ys)
plt.axis([0,50,0,25])
plt.title("Histogram of number of friends")
plt.xlabel("Number of friends")
plt.ylabel("Number of members")
plt.show()