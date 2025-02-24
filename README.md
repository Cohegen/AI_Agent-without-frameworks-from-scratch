# AI_Agent-without-frameworks-from-scratch
# AI Agent: Deep Learning & Machine Learning Explainer

## Overview
This is a simple AI agent built from scratch in Python that explains concepts related to Deep Learning and Machine Learning. The agent processes user queries, searches a knowledge base, and provides detailed explanations. It does not rely on external frameworks, keeping the implementation minimalistic and easy to understand.

## Features
- Processes user queries and extracts relevant keywords.
- Searches an internal knowledge base for explanations.
- Provides detailed responses about deep learning and machine learning topics.
- Runs in an interactive command-line interface.
- Modular design with separate Python scripts for different functionalities.

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.7+ recommended). You can check your Python version with:
```bash
python --version
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/ai-agent-explainer.git
cd ai-agent-explainer
```

### Run the AI Agent
```bash
python main.py
```

## Usage
After running `main.py`, the AI agent will prompt you to enter a query. You can ask questions like:
```
You: What is deep learning?
AI Agent:
Deep Learning:
Deep learning is a subset of machine learning that uses neural networks with many layers (deep neural networks) to model complex patterns in data. It has been highly successful in image recognition, speech recognition, natural language processing, and more.
```

To exit the program, type `exit`, `quit`, or `bye`.

## Project Structure
```
├── query_processing.py   # Cleans and extracts keywords from user queries
├── knowledge_base.py     # Contains knowledge entries and searches them
├── response_generator.py # Matches queries with knowledge and generates responses
├── main.py               # Runs the interactive AI agent
└── README.md             # Documentation for the project
```

## How It Works
1. **Query Processing:**
   - Cleans the user’s input (lowercases, removes special characters, extracts keywords).
2. **Knowledge Base Search:**
   - Searches predefined knowledge entries for matching keywords.
3. **Response Generation:**
   - Returns explanations for found topics or asks for clarification.
4. **Main Loop:**
   - Runs continuously until the user exits.

## Future Improvements
- Expand the knowledge base with more ML/DL topics.
- Improve NLP capabilities for better query understanding.
- Add interactive follow-up questions for deeper explanations.
- Implement a web interface using Flask or FastAPI.

## License
This project is open-source under the [MIT License](LICENSE).

## Contributions
Feel free to contribute by adding new topics, improving explanations, or enhancing the code structure. Submit a pull request or open an issue for discussions.

## Contact
For any inquiries or feedback, reach out via anthonynjenga143@gmail.com.

