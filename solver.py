#
#This script uses the Finite Difference Method to simulate heat spreading across a metal plate. 
# It is designed to run in a loop, simulating "real-time" scientific processing.
#########################################

import numpy as np
import time
import logging

# Configure logging to see output in 'kubectl logs'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def solve_heat_equation(size=50, iterations=100, alpha=0.01):
    """
    Simulates 2D Heat Diffusion on a square grid.
    Equation: du/dt = alpha * (d2u/dx2 + d2u/dy2)
    """
    # Initialise a cold plate (0 degrees) with a hot center (100 degrees)
    u = np.zeros((size, size))
    u[size//2, size//2] = 100.0
    
    # Finite Difference Method
    for i in range(iterations):
        u_new = u.copy()
        # Vectorised stencil operation for 2D diffusion
        u_new[1:-1, 1:-1] = u[1:-1, 1:-1] + alpha * (
            u[2:, 1:-1] + u[:-2, 1:-1] + 
            u[1:-1, 2:] + u[1:-1, :-2] - 
            4 * u[1:-1, 1:-1]
        )
        u = u_new
        
        if i % 20 == 0:
            avg_temp = np.mean(u)
            logging.info(f"Iteration {i}: Average Plate Temperature = {avg_temp:.4f}°C")
        
    return np.mean(u)

if __name__ == "__main__":
    logging.info("ThermaKube Solver Initialised.")
    while True:
        final_temp = solve_heat_equation()
        logging.info("Simulation cycle complete. Restarting in 10 seconds...")
        time.sleep(10)
