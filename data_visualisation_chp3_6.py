from matplotlib import pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i, _ in enumerate(variance)]
# Multiply call of plt.plot
# Many series in the same grph
# Green line continue
plt.plot(xs,variance,'g-',label='variance')
# red line alternant small points and in-lines
plt.plot(xs,bias_squared,'r-',label='bias^2')
# blue line small points
plt.plot(xs,total_error,'b:',label='total error')
# Every serie have a label
# We have an automatic legend
# loc=9 signify "top center" (middle hight center )
plt.legend(loc=9)
plt.xlabel("Complexity of the model")
plt.xticks([])
plt.title("Compromise between biais and variance")
plt.show()

