# Importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

our_data = pd.read_csv("insurance.csv")

# identifying the coloumns of data that will be used for x and y axis
x = our_data.iloc[:,:1].values.reshape(-1,1)
y = our_data.iloc[:,-1].values


# Choosing data points colour, laybling the axis and ploting graph
plt.scatter(x,y,color = 'b')
plt.xlabel('Age (Years)')
plt.ylabel('Charges (Pounds)')
plt.show()

# fitting a linear regerssion model
linear_model = LinearRegression()

linear_model.fit(x,y) 

# Plotting data with line of best fit
y_pred = linear_model.predict(x)

plt.figure()
plt.scatter(x,y,color = 'b')
plt.plot(x,y_pred,color = 'r')
plt.xlabel('Age (Years)')
plt.ylabel('Charges (Pounds)')
plt.show()

# Predict an unknown value, user is asked to input age for which a predicted charges is printed.

unk_x = [[int(input("What age would you like to predicted charges for?\n"))]]

x_pred = np.append(x, unk_x).reshape(-1,1)
y_pred = linear_model.predict(x_pred)

print("Expected charges for age is £", linear_model.predict(unk_x))