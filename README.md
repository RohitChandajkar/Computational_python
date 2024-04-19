# Computational_python
## Lagrange Interpolation for Ideal Gas and Linear Equation Solver

This project involves two tasks:

### Lagrange Interpolation for Ideal Gas

Given a set of data points representing the relationship between temperature (°C) and pressure (atm) of an ideal gas, this task aims to find the polynomial P(T) that approximates this relationship using Lagrange interpolation. 

#### Project Steps:

1. **Lagrange Interpolation Function (`lagrange_interpolation`)**:
   - Implement a Python function named `lagrange_interpolation` that takes two arrays `x` and `y` representing the data points and a value `x_val` at which to interpolate, and returns the interpolated value `y_val`.

2. **Interpolation Script**:
   - Develop a Python script to interpolate the pressure at temperatures of 10°C, 30°C, 50°C, 70°C, and 90°C using the Lagrange interpolation function created in step 1.

3. **Visualization**:
   - Plot the interpolated pressure values along with the given data points on a graph to visualize the accuracy of the interpolation.

### Linear Equation Solver

Given a system of linear equations represented as the matrix equation Ax = b, where:
\[A = \begin{bmatrix} 2 & 3 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{bmatrix}\]
and
\[b = \begin{bmatrix} 7 \\ 5 \\ 12 \end{bmatrix}\]

This task involves solving the system of linear equations to find the values of x, y, and z.

#### Project Steps:

1. **Linear Equation Solver Function (`linear_equation_solver`)**:
   - Write a Python function named `linear_equation_solver` that takes matrix A and vector b as inputs and returns the solution vector x.

2. **Usage Script**:
   - Implement a Python script to solve the given system of linear equations using the `linear_equation_solver` function.



To use the Lagrange interpolation function and solve the system of linear equations, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the project directory.
4. Run the interpolation script (`interpolation_script.py`) to perform Lagrange interpolation.
5. Run the linear equation solver script (`linear_equation_solver_script.py`) to solve the system of linear equations.
6. Review the generated plots and output to analyze the results.

### Requirements

- Python 3.x
- NumPy
- Matplotlib
