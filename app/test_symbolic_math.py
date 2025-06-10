from symbolic_math import solve_math_problem

def test_math_solver():
    problem = "x + 5 = 10"
    solution = solve_math_problem(problem)
    print(f"Problem: {problem}")
    print(f"Solution: {solution}")

if __name__ == "__main__":
    test_math_solver()