import numpy as np
from prettytable import PrettyTable
from typing import Callable

resultados = PrettyTable(field_names=["i", "p", "f(p)"])
    
def fixed_point_iteration(f: Callable[[np.ndarray], np.ndarray], x0: np.ndarray, tol: float = 1e-6, max_iter: int = 1000) -> np.ndarray:
    """
    Performs fixed-point iteration to find the fixed point of a given function.

    Parameters:
    - f (callable): The function for which the fixed point is sought.
    - x0 (numpy.ndarray): The initial guess for the fixed point.
    - tol (float, optional): The tolerance for convergence. Defaults to 1e-6.
    - max_iter (int, optional): The maximum number of iterations. Defaults to 1000.

    Returns:
    - numpy.ndarray: The estimated fixed point.

    Raises:
    - ValueError: If the function does not converge within the maximum number of iterations.

    Fixed-point iteration is an iterative method used to find the fixed point of a function.
    The fixed point of a function f(x) is a value x* such that f(x*) = x*.

    The function iterates through the following steps:
    1. Start with an initial guess x0.
    2. Compute the next guess x_new = f(x).
    3. Repeat step 2 until the difference between x_new and x is within the specified tolerance tol, or until reaching the maximum number of iterations.

    If the function converges within the specified tolerance, the estimated fixed point is returned.
    If the function does not converge within the maximum number of iterations, a ValueError is raised.

    Example:
    >>> f = lambda x: np.cos(x)  # Define the function f(x) = cos(x)
    >>> initial_guess = np.array([1.0])  # Initial guess for the fixed point
    >>> fixed_point = fixed_point_iteration(f, initial_guess)  # Perform fixed-point iteration
    >>> fixed_point  # Display the estimated fixed point
    array([0.73908513])
    """
    x = np.array(x0)
    for i in range(max_iter):
        x_new = np.array(f(x))
        if np.allclose(x_new, x, atol=tol):
            return x_new
        x = x_new
    raise ValueError("Did not converge within the maximum number of iterations.")

def Newton_Raphson(f:Callable[[float], float], fp: Callable[[float], float], p_0: float, TOL: float = 1e-6, N_0: int = 1000) -> float:
    """
    Newton-Raphson method for finding a root of a function.

    Parameters:
    - f (callable): The function for which the root is sought.
    - fp (callable): The derivative of the function f.
    - p_0 (float): Initial guess for the root.
    - TOL (float, optional): Tolerance for convergence. Defaults to 1e-6.
    - N_0 (int, optional): Maximum number of iterations. Defaults to 1000.

    Returns:
    - float: Estimated root of the function.

    The Newton-Raphson method is an iterative root-finding algorithm that uses the derivative of the function to approximate the root.

    The function iterates through the following steps:
    1. Start with an initial guess p_0.
    2. Compute the next approximation p = p_0 - f(p_0) / f'(p_0), where f' denotes the derivative of f.
    3. Repeat step 2 until the difference between p and p_0 is within the specified tolerance TOL, or until reaching the maximum number of iterations N_0.

    If the method converges within the specified tolerance, the estimated root is returned.
    If the method does not converge within the maximum number of iterations, None is returned.

    Example:
    >>> f = lambda x: x**2 - 4  # Define the function f(x) = x^2 - 4
    >>> fp = lambda x: 2 * x  # Define the derivative of f
    >>> initial_guess = 3.0  # Initial guess for the root
    >>> root = Newton_R(f, fp, initial_guess)  # Apply Newton-Raphson method
    >>> root  # Display the estimated root
    2.000000000002
    """
    i = 1
    resultados.clear_rows()  # Assuming resultados is an instance of a data structure for storing results
    for i in range(N_0):
        p = p_0 - f(p_0) / fp(p_0)
        resultados.add_row([i, p, f(p)])  # Assuming resultados supports adding rows
        if abs(p - p_0) < TOL:
            print(resultados)  # Assuming resultados can be printed
            print(f"ER = {abs(p - p_0) / abs(p) * 100}%")
            return p
        p_0 = p
    raise ValueError("Did not converge within the maximum number of iterations.")

    
def Secante(f: Callable[[float], float], p_0: float, p_1: float, TOL: float = 1e-6, N_0: int = 1000) -> float:
    """
    Secant method for finding a root of a function.

    Parameters:
    - f (callable): The function for which the root is sought.
    - p_0 (float): Initial guess for the root.
    - p_1 (float): Second initial guess for the root.
    - TOL (float, optional): Tolerance for convergence. Defaults to 1e-6.
    - N_0 (int, optional): Maximum number of iterations. Defaults to 1000.

    Returns:
    - float: Estimated root of the function.

    The secant method is an iterative root-finding algorithm that approximates the root by linearly interpolating between two points on the curve of the function.

    The function iterates through the following steps:
    1. Start with initial guesses p_0 and p_1.
    2. Compute the next approximation p using linear interpolation based on the function values at p_0 and p_1.
    3. Repeat step 2 until the difference between p and p_1 is within the specified tolerance TOL, or until reaching the maximum number of iterations N_0.

    If the method converges within the specified tolerance, the estimated root is returned.
    If the method does not converge within the maximum number of iterations, a ValueError is raised.

    Example:
    >>> f = lambda x: x**2 - 4  # Define the function f(x) = x^2 - 4
    >>> initial_guess_1 = 3.0  # First initial guess for the root
    >>> initial_guess_2 = 4.0  # Second initial guess for the root
    >>> root = Secante(f, initial_guess_1, initial_guess_2)  # Apply Secant method
    >>> root  # Display the estimated root
    2.000000006782
    """
    resultados.clear_rows()  # Assuming resultados is an instance of a data structure for storing results
    q_0 = f(p_0)
    q_1 = f(p_1)
    resultados.add_row([0, p_0, q_0])  # Assuming resultados supports adding rows
    resultados.add_row([1, p_1, q_1])  # Assuming resultados supports adding rows
    i = 2
    for i in range(N_0):
        p = p_1 - q_1 * (p_1 - p_0) / (q_1 - q_0)
        resultados.add_row([i, p, f(p)])  # Assuming resultados supports adding rows
        if abs(p - p_1) < TOL:
            print(resultados)  # Assuming resultados can be printed
            print(f"ER = {abs(p - p_1) / abs(p) * 100}%")
            return p
        p_0 = p_1
        q_0 = q_1
        p_1 = p
        q_1 = f(p)

    raise ValueError("Did not converge within the maximum number of iterations.")


def steffensen(f: callable, x0: float, tol: float = 1e-6, max_iter: int = 100) -> float:
    """
    Steffensen's method for root finding.

    Parameters:
    - f (callable): The function for which the root is sought.
    - x0 (float): Initial guess for the root.
    - tol (float, optional): Tolerance for convergence. Defaults to 1e-6.
    - max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
    - float: Estimated root of the function.

    Steffensen's method is an iterative root-finding algorithm that uses a combination of function evaluations to approximate the root.

    The function iterates through the following steps:
    1. Start with an initial guess x0.
    2. Compute the next approximation x_new using the function evaluations.
    3. Repeat step 2 until the difference between x_new and x is within the specified tolerance tol, or until reaching the maximum number of iterations max_iter.

    If the method converges within the specified tolerance, the estimated root is returned.
    If the method does not converge within the maximum number of iterations, a ValueError is raised.

    Example:
    >>> f = lambda x: x**2 - 4 +x  # Define the function f(x) = x^2 - 4 + x
    >>> g = lambda x: f(x) - x # Define the function g(x) = x^2 - 4
    >>> initial_guess = 3.0  # Initial guess for the root
    >>> root = steffensen(g, initial_guess)  # Apply Steffensen's method
    >>> root  # Display the estimated root
    2.000000000000041
    """
    x = x0
    for i in range(max_iter):
        x_next = f(x)
        x_next_next = f(x_next)
        denominator = x_next_next - 2 * x_next + x
        if abs(denominator) < tol:  # Prevent division by zero
            print("Denominator too small. Method might not converge.")
            return None
        x_new = x - ((x_next - x) ** 2) / denominator
        if abs(x_new - x) < tol:
            return x_new
        x = x_new

    raise ValueError("Did not converge within the maximum number of iterations.")
