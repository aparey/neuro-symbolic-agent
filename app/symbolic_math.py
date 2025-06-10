import sympy as sp
from llm_interface import parse_with_llm

def parse_math_problem(problem_text):
    """
    Parse a natural language math problem into a SymPy expression using an LLM.
    """
    symbolic_expr = parse_with_llm(problem_text)
    try:
        expr = sp.sympify(symbolic_expr)
        return expr
    except Exception as e:
        raise ValueError(f"Failed to convert LLM output to SymPy expression: {e}")

def solve_math_problem(problem_text):
    """
    Solve a math problem given in natural language.
    Returns the solution as a string.
    """
    try:
        expr = parse_math_problem(problem_text)
        solution = sp.solve(expr)
        return str(solution)
    except Exception as e:
        return f"Error solving problem: {e}"
