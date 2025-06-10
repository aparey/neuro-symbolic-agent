# Neuro-Symbolic Reasoning Agent

A modular Python project that combines symbolic and neural approaches to solve math, visual, and logic reasoning tasks. The system supports:
- **Math Reasoning**: Symbolic math solving (with optional LLM/NLP parsing)
- **Visual Reasoning**: OCR-based extraction and math solving from images, with hooks for VQA
- **Logic Reasoning**: Prolog-based logic queries (e.g., transitive relationships)

## Project Structure
```
app/
  ├── symbolic_math.py        # Math reasoning (SymPy, optional LLM)
  ├── visual_parser.py        # Visual reasoning (OCR, image Q&A)
  ├── symbolic_logic.py       # Logic reasoning (Prolog via PySWIP)
  ├── pipeline.py             # CLI pipeline for all modes
  ├── streamlit_app.py        # (Optional) Streamlit web UI
  ├── __init__.py
  └── test_*.py               # Test scripts for each module

data/                         # Datasets (GSM8K, CLEVR, Winograd, etc.)
models/                       # (Optional) Pretrained models for VQA/LLM
```

## Features
- **Math**: Solve equations like `x + 5 = 10` or extract and solve from images.
- **Visual**: OCR for math in images; placeholder for VQA.
- **Logic**: Add facts/rules and run queries (e.g., "Is Alice taller than Charlie?").

## Setup
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # For OCR:
   brew install tesseract  # (macOS)
   # or
   sudo apt-get install tesseract-ocr  # (Linux)
   ```
3. **(Optional) Download datasets**
   - Place datasets in the `data/` folder as needed.

## Usage
### CLI Pipeline
```bash
python app/pipeline.py
```
- Select mode: Math, Visual, or Logic
- Follow prompts for input

### Streamlit Web App
```bash
streamlit run app/streamlit_app.py
```
- Use the sidebar to select reasoning mode
- Enter problems, upload images, or run logic queries interactively

## Example Logic Test
```
Facts:
  taller(alice, bob)
  taller(bob, charlie)
Rule:
  taller(X, Y) :- taller(X, Z), taller(Z, Y)
Query:
  taller(alice, charlie)  # True (transitive)
```

## Notes
- For LLM-based math parsing, set your OpenAI API key as an environment variable (`OPENAI_API_KEY`).
- For visual reasoning, Tesseract OCR must be installed and available in your PATH.
- The `models/` directory is reserved for future VQA or LLM models.

## Contributing
Pull requests and suggestions are welcome!

## License
[MIT License](LICENSE)
