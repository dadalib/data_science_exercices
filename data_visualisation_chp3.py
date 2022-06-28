# Add comments
import sys

print("Version",sys.version)
print("FILE",sys.executable)
import matplotlib
from matplotlib import pyplot as plt
years = [1950,1960,1970,1980,2000,2010]
gdp = [300.2,543.3,1075.3,2862.5,5979.6,10289.7,14958.3]

# Graph with x as years and y as PIB
plt.plot(years,gdp, color='green',marker='o',linestyle='solid')
# Add a tittle
plt.tittle("Valeurs de GDP")
# Add label in y
plt.ylabel("Millard des dollars")
plt.show()
