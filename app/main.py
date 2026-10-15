from app.llm import ask_llm

def main() -> None:
    print("AI Knowledge Assistant — LLM Test")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGood Bye!")
            break
        
        if question.lower() in {"exit", "quit"}:
            print("Good Bye!")
            break
        if not question:
            print("Please enter a question.\n")
            continue
        try:
            answer = ask_llm(question)
            print(f"Assistant: {answer}\n")
        except ValueError as e:
            print(f"\nConfiguration or input error: {e}\n")
        except Exception as e:
            # Do not print credentials or request headers.
            print(
                "\nThe LLM request failed. Check your API key, "
                "model access, network connection, and API usage limits."
            )
            print(f"Error type: {type(e).__name__}\n")

if __name__ == "__main__":
    main()