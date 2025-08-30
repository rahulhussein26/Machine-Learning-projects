# Importing relevent libraries 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

# Data imported from a csv file and read 
filename = "/Users/rahulhussein/Desktop/Dummy experimental data /StefanBoltzmann_example (1).csv"
data = pd.read_csv(filename)
data_df = pd.DataFrame(data)


# Defining function now 
