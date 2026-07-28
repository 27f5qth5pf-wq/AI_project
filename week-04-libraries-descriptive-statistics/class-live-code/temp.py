import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


day = ['mon','tue','wen','thu','fri','sat','sun']
temp = [37.3, 38.5, 45.5, 37.3,26.7,.6,39.2]


plt.plot(day,temp)
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.show()