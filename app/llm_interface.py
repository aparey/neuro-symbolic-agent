import os
import openai

# Set your OpenAI API key here or via environment variable
# openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_with_llm(problem_text):
    """
    Use an LLM (OpenAI) to parse a natural language math problem into a symbolic expression.
    Returns the parsed expression as a string.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts natural language math problems into symbolic expressions. Respond with only the symbolic expression."},
                {"role": "user", "content": problem_text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error parsing with LLM: {e}"
