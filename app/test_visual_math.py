from visual_parser import extract_text_from_image
from symbolic_math import solve_math_problem

# Updated with the provided image file path
image_path = "/Users/parey69/Desktop/group project/neuro_symbolic_agent/visual_test_image.png"

# Step 1: OCR - Extract equation text from image
extracted_text = extract_text_from_image(image_path)
print(f"Extracted text: {extracted_text}")

# Step 2: Math Reasoning - Solve the extracted equation
solution = solve_math_problem(extracted_text)
print(f"Solution: {solution}") 