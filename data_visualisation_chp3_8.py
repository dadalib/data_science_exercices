from matplotlib import pyplot as plt

test_1_grades = [99,90,85,97,80]
test_2_grades = [100,85,60,90,70]

plt.scatter(test_1_grades,test_2_grades)
plt.title("Les axes ne sont pas comparables")
plt.xlabel("Notes au test 1")
plt.ylabel("Notes au test 2")
plt.axis("equal")
plt.show()

