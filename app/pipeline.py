import sys
from symbolic_math import solve_math_problem
from visual_parser import extract_text_from_image, answer_visual_question
from symbolic_logic import SymbolicLogicReasoner


def run_math_mode():
    problem = input("Enter a math problem (e.g., 'x + 5 = 10'): ")
    solution = solve_math_problem(problem)
    print(f"Solution: {solution}")

def run_visual_mode():
    image_path = input("Enter the path to the image file: ")
    question = input("Enter your question about the image (or leave blank to extract text): ")
    if question.strip() == "":
        extracted_text = extract_text_from_image(image_path)
        print(f"Extracted text: {extracted_text}")
        solution = solve_math_problem(extracted_text)
        print(f"Math Solution: {solution}")
    else:
        answer = answer_visual_question(image_path, question)
        print(f"Answer: {answer}")

def run_logic_mode():
    reasoner = SymbolicLogicReasoner()
    print("Enter logic facts (e.g., 'taller(alice, bob)'). Type 'done' when finished:")
    while True:
        fact = input("Fact: ")
        if fact.strip().lower() == 'done':
            break
        reasoner.add_fact(fact)
    print("Enter logic rules (e.g., 'taller(X, Y) :- taller(X, Z), taller(Z, Y)'). Type 'done' when finished:")
    while True:
        rule = input("Rule: ")
        if rule.strip().lower() == 'done':
            break
        reasoner.add_rule(rule)
    while True:
        query = input("Enter a query (e.g., 'taller(alice, charlie)') or 'exit' to quit: ")
        if query.strip().lower() == 'exit':
            break
        result = reasoner.query(query)
        print(f"Result: {bool(result)} (Details: {result})")

def main():
    print("Select reasoning mode:")
    print("1. Math")
    print("2. Visual")
    print("3. Logic")
    mode = input("Enter 1, 2, or 3: ")
    if mode == '1':
        run_math_mode()
    elif mode == '2':
        run_visual_mode()
    elif mode == '3':
        run_logic_mode()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
