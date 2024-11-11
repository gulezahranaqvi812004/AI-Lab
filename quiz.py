import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
array =np.random.randint(1, 51, size=(3, 3))
print(array)
dataset = {'name' : ['a' , 'b', 'c'],
            'Age' : ['40' , '70', '30'],
            'City': ['N', '', 'C' ]} 
df = pd.DataFrame(dataset)
filtered_age = df[pd.to_numeric(df['Age'])<20]
print(filtered_age)
df['Salary']=100000
df=df.dropna
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of X vs Y')
plt.show()