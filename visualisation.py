# lets see how is building permit in each region by plotting histogram plot

import matplotlib.pyplot as plt
import seaborn as sns
from run3 import df
sns.set()
plt.hist(df['Zipcode'], bins = 27)
plt.xlabel('Zipcode')
plt.ylabel('total of building permits in each region')
plt.show()

