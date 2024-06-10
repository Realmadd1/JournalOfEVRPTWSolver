from main.EVRPTWPlanner import EVRPTWSolver


if __name__ == "__main__":
    path = "instances/c101.txt"
    solver = EVRPTWSolver()
    solver.run(path)
