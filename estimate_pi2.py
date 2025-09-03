import argparse
import numpy as np

def estimate_pi(num_points: int, seed: int = None):
    """
    Estimates the value of Pi using the Monte Carlo method.
    Args:
    num_points: The number of random points to generate.
    seed: An optional random seed for reproducibility.
    """
    # 1. Use the seed if it’s provided
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random points between-1 and 1 for both x and y axes
    x_coords = np.random.uniform(-1, 1, num_points)
    y_coords = np.random.uniform(-1, 1, num_points)
    
    # Calculate the distance of each point from the origin
    distances = x_coords**2 + y_coords**2
    points_inside_circle = np.sum(distances <= 1)
    
    # Estimate Pi
    pi_estimate = 4 * points_inside_circle / num_points
    print(f"Number of points: {num_points}")
    print(f"Points inside circle: {points_inside_circle}")
    print(f"Estimated value of Pi: {pi_estimate}")
    print(f"Seed used: {seed}")

def main():
    """Main function to parse arguments and run the estimation."""
    # 2. Set up the argument parser
    parser = argparse.ArgumentParser(description="Estimate Pi using Monte Carlo simulation.")
    parser.add_argument(
        "--num-points",
        type=int,
        default=100000,
        help="Number of random points to generate."
    )
    
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility."
    )
    args = parser.parse_args()
    
    # 3. Call our function with the parsed arguments
    estimate_pi(num_points=args.num_points, seed=args.seed)

if __name__ == "__main__":
    main()