# 🧠 AI Algorithms

This project implements several fundamental **AI search algorithms** to solve classic problems like Frozen Lake, Ant Maze (Taxi-v3), and Traveling Salesman Problem (TSP). The following algorithms are included:

- 🔍 Branch and Bound
- ⭐ IDA* (Iterative Deepening A*)
- 🧗 Hill Climbing
- 🔥 Simulated Annealing

---

## 📁 Project Structure

*   `AI-Algorithms`
    *   `algorithms/` - Contains all the algorithms.
        * `__pycache__/` - folder for the cache.
        * `branch_and_bound.py` - branch and bound algorithms
        * `hill_climbing.py` - hill climbing algorithms
        * `ida_star.py` - IDA* algorithm
        * `simulated_annealing.py` - simulated annealing algorithm
    *   `environments/` - All the environments file for the diffrent algorithms.
        * `__pycache__/` - folder for the cache.
        * `ant_maze_env.py` - environment for the IDA* 
        * `fronzen_lake_env.py` - enviroment for BnB 
        * `tsp_env.py` - environment for hill climbing and simulated annealing
    *   `scripts/` - Run script of algorithams and script to test environments.
        * `__pycache__/` - folder for the cache.
        * `run_algorithms.py` - script to run all the algorithm at once in it's respective environment 
        * `test_env.py` - script for testing for the all the environments 
    *   `README.md` - Readme file.

---

## ⚙️ Setup Instructions (In Ubuntu / Linux)

### 1. Clone the Repository

```bash
git clone https://github.com/Hitman-45/AI-Algorithms.git
cd AI-Algorithms
```

### 2. Setup for the enviroment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install gymnasium for the algorithms
```bash
pip install --upgrade pip
pip install gymnasium[toy-text]
```
### 4. Script to run all the algorithams using script file... 
```bash
PYTHONPATH=. python3 scripts/run_algorithms.py
```