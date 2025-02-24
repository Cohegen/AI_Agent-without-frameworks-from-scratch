from response_generator import generate_response

def run_ai_agent():
    print("AI Agent: Hello! Ask me anything about AI, Python, or Machine Learning.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI Agent: Goodbye!")
            break
        
        response = generate_response(user_input)
        print(f"AI Agent: {response}")

if __name__ == "__main__":
    run_ai_agent()
