# agentic-ai
It is a pilot project for developing an AI Agent from scratch.
The programming language used here is Python and version 3.13 with pip.
The framework LangChain is preferred
I am using OpenAI API Key in this porject
I am using MongoDB as the storage for embedding and vector searching
Currenttly the local CMD can be used for intercting with the ChatBot

#To activate the virtual environment
1. run .\virtual-env\Scripts\activate (Windows)
2. run source venv/bin/activate (bash/zsh)

#To run the project
run python -m app.main

#To keep running the project while you make the changes
python -m watchfiles --filter python '.\virtual-env\Scripts\python -m app.main' .\app