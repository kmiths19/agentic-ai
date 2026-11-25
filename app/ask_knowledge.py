
from app.rag import ask_knowledge_base
from app.llm import ask_llm

def main() -> None:
    print("Hi! I'm Golku, your assistant.")
    print("You can ask me questions in your language.")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            result = ask_knowledge_base(question)

            print(f"\nGolku: {result['answer']}")

            if result["sources"]:
                print("\nSources:")
                for source in result["sources"]:
                    print(f"- {source}")

            print()

        except ValueError as error:
            print(f"\nInput error: {error}\n")
        except Exception as error:
            print("\nThe question could not be processed.")
            print(f"Error type: {type(error).__name__}\n")


if __name__ == "__main__":
    main()
