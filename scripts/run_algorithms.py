import time
from algorithms.branch_and_bound import branch_and_bound
from algorithms.ida_star import ida_star
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from environments.frozen_lake_env import frozen_lake_env
from environments.ant_maze_env import ant_maze_env
from environments.tsp_env import generate_tsp_env

def run_frozen_lake():
    env = frozen_lake_env()
    start_time = time.time()
    path, cost = branch_and_bound()
    end_time = time.time()
    print(f"** BnB Solution: {path} \n** Cost: {cost} \n** Time Taken: {end_time - start_time:.4f} sec")

def run_ant_maze():
    env = ant_maze_env()
    start_time = time.time()
    path, cost = ida_star()
    end_time = time.time()
    print(f"** IDA* Solution: {path} \n**  Cost: {cost} \n**  Time Taken: {end_time - start_time:.4f} sec")

def run_tsp():
    distance_matrix = generate_tsp_env(5)
    start_time = time.time()
    hc_path, hc_cost = hill_climbing(distance_matrix)
    end_time = time.time()
    print(f"** Hill Climbing Solution: {hc_path} \n**  Cost: {hc_cost} \n**  Time Taken: {end_time - start_time:.4f} sec \n")

    start_time = time.time()
    sa_path, sa_cost = simulated_annealing(distance_matrix)
    end_time = time.time()
    print(f"** Simulated Annealing Solution: {sa_path} \n**  Cost: {sa_cost} \n**  Time Taken: {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    print("Running Frozen Lake (Branch and Bound)")
    run_frozen_lake()
    print("\nRunning Ant Maze (IDA*)")
    run_ant_maze()
    print("\nRunning Traveling Salesman Problem (Hill Climbing & Simulated Annealing)")
    run_tsp()