import streamlit as st
from symbolic_math import solve_math_problem
from visual_parser import extract_text_from_image, answer_visual_question
from symbolic_logic import SymbolicLogicReasoner
import os

st.title("Neuro-Symbolic Reasoning Agent")

mode = st.sidebar.selectbox("Select Reasoning Mode", ("Math", "Visual", "Logic"))

if mode == "Math":
    st.header("Math Reasoning")
    problem = st.text_input("Enter a math problem (e.g., 'x + 5 = 10'):")
    if st.button("Solve") and problem:
        solution = solve_math_problem(problem)
        st.success(f"Solution: {solution}")

elif mode == "Visual":
    st.header("Visual Reasoning")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    question = st.text_input("Enter your question about the image (or leave blank to extract text):")
    if uploaded_file is not None:
        image_path = os.path.join("temp_uploaded_image.png")
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(image_path, caption="Uploaded Image", use_column_width=True)
        if st.button("Process Image"):
            if question.strip() == "":
                extracted_text = extract_text_from_image(image_path)
                st.info(f"Extracted text: {extracted_text}")
                solution = solve_math_problem(extracted_text)
                st.success(f"Math Solution: {solution}")
            else:
                answer = answer_visual_question(image_path, question)
                st.success(f"Answer: {answer}")

elif mode == "Logic":
    st.header("Logic Reasoning")
    st.write("Enter logic facts and rules, then query the knowledge base.")
    facts = st.text_area("Facts (one per line, e.g., 'taller(alice, bob)'):")
    rules = st.text_area("Rules (one per line, e.g., 'taller(X, Y) :- taller(X, Z), taller(Z, Y)'):")
    query = st.text_input("Query (e.g., 'taller(alice, charlie)'):")
    if st.button("Run Logic Query") and query:
        reasoner = SymbolicLogicReasoner()
        for fact in facts.strip().splitlines():
            if fact.strip():
                reasoner.add_fact(fact.strip())
        for rule in rules.strip().splitlines():
            if rule.strip():
                reasoner.add_rule(rule.strip())
        result = reasoner.query(query)
        st.success(f"Result: {bool(result)} (Details: {result})") 