#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Check if requirements are installed
if ! pip show streamlit > /dev/null; then
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

# Start the Streamlit app
streamlit run ui/streamlit_app.py
