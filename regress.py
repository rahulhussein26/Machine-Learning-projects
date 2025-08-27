import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats 

x = np.arange(0, 4*np.pi, step=0.01)
y = np.sin(x)

plt.figure(figsize=(10,8))
plt.plot(x,y)
plt.grid(True)


x_val = np.arange(0, 45, step=5)
print(x_val)

print(x_val)

y_val = [i for i in x_val if i == 2*i]
y_list = [] 

for i in x_val: 
    y = 2*i 
    y_list.append(y)

print("checking if the y values are properly working")

print(y_list)
y_list_new = [] 


for i in y_list: 
    whl_num = int(i)
    y_list_new.append(whl_num)
    
    
slope, intercept, r, p, std_err = stats.linregress(x_val, y_list_new)

def func(x):
    return slope*x_val + intercept


# need to create the model 