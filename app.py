import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")

# Initialize LangChain components
def initialize_prompt():
    """Create the chat prompt template."""
    return ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Please respond to the question asked."),
            ("user", "Question: {question}")
        ]
    )

def initialize_llm():
    """Initialize the Ollama LLM with the Gemma model."""
    return Ollama(model="gemma2:2b")

def initialize_chain(prompt, llm, parser):
    """Compose the processing chain."""
    return prompt | llm | parser

# Streamlit framework
def main():
    """Main function to run the Streamlit app."""
    st.title("Simple LangChain Gen AI App - Gemma2 Model")
    
    # User input
    input_text = st.text_input("What question do you have in mind?")
    
    # Initialize components
    prompt = initialize_prompt()
    llm = initialize_llm()
    output_parser = StrOutputParser()
    chain = initialize_chain(prompt, llm, output_parser)
    
    # Button to generate answer
    if st.button("Generate Answer"):
        if not input_text.strip():
            st.error("Please enter a question before clicking Generate Answer.")
            return

        try:
            result = chain.invoke({"question": input_text.strip()})
            st.markdown(f"**Answer:** {result}")
        except Exception as e:
            st.error(f"Oops! An error occurred: {e}")

if __name__ == "__main__":
    main()
