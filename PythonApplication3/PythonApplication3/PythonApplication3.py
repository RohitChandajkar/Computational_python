import numpy as np
import matplotlib.pyplot as plt

def lagrange_Interpolation(x, y, x_val):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term 
    return result           
    
x = np.array([0, 20, 40, 60, 80, 100], float)
y = np.array([1.000, 0.889, 0.745, 0.582, 0.412, 0.248], float)

temperature_to_interpolation = [10, 30, 50, 70, 90]
interpolated_pressures = []

# Interpolate pressures
for temp in temperature_to_interpolation:
    interpolated_pressure = lagrange_Interpolation(x, y, temp)
    interpolated_pressures.append(interpolated_pressure)

# Plotting
plt.plot(x, y, 'bo-', label='Given Data')
plt.plot(temperature_to_interpolation, interpolated_pressures, 'rx', label='Interpolated Values')
plt.xlabel('Temperature (\u00b0C)')  # Using Unicode escape sequence for the degree symbol
plt.ylabel('Pressure')
plt.title('Interpolated Pressure Values')
plt.legend()
plt.grid(True)
plt.show()
