from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import sys
sys.stdout.flush()

template = """
Answer the question below

Here is the conversation history:{context}

Question:{question}

Answer:

"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("YOU: ")
        if user_input.lower() =="exit":
            break

        result = chain.invoke({"context": context,"question": user_input})
        answer = str(result)
        print("Bot:", answer,flush=True)
        context += f"\nUser: {user_input}\nAI: {answer}"


if __name__ == "__main__":
    handle_conversation()
