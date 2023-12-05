import os
import subprocess
import time

def run_solution(file_path, file):
    start_time = time.time()

    try:
        # Run the solution using subprocess
        result = subprocess.run(['python3', file_path], capture_output=True, text=True, timeout=3)
        # Assuming the solutions print the output to the console
        output = result.stdout.strip()

        if output:
            print("######################")
            print()
            print(f"{file[:3]} {file[3:-6]} Part {file[-4]}")
            print("Solution:", output)
        else:
            return 0

    except subprocess.TimeoutExpired:
        print("Timeout: The program took too long to run.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time: {elapsed_time:.5f} seconds")
    print()
    return elapsed_time

def main():
    # Get the current script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    d = 5
    days = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7", "Day8","Day9","Day10","Day11","Day12","Day13","Day14","Day15","Day16","Day17","Day18","Day19","Day20","Day21","Day22","Day23","Day24","Day25"]
    # List all files in the current script's directory and sort them
    files = sorted([f for f in os.listdir(script_dir) if any(day in f for day in days[:d])])

    total_time = 0.0

    # Run each solution in the folder
    for file in files:
        file_path = os.path.join(script_dir, file)
        total_time += run_solution(file_path, file)

    print("######################")
    print(f"Total Time Used: {total_time:.5f} seconds")  

if __name__ == "__main__":
    main()
