from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv
load_dotenv()

class SupportAgent:
    def __init__(self):
        # Load and process documents
        product_docs = TextLoader('knowledge_base/products.txt').load()
        policy_docs = TextLoader('knowledge_base/policies.txt').load()
        all_docs = product_docs + policy_docs

        # Split documents into sections
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n"]
        )
        splits = text_splitter.split_documents(all_docs)

        # Create vector store
        self.vector_store = Chroma.from_documents(
            documents=splits,
            embedding=OpenAIEmbeddings(),
            persist_directory="./chroma_db"
        )

        # Define system prompt
        system_prompt = SystemMessagePromptTemplate.from_template(
            "You are a friendly and helpful customer support agent for an e-commerce store. "
            "Your goal is to assist customers with their questions about products and policies. "
            "Use the following context to answer the customer's question. "
            "Always respond in a polite and professional tone. "
            "If you don't know the answer, apologize and suggest contacting support directly.\n\n"
            "Context:\n{context}"
        )

        # Define human prompt
        human_prompt = HumanMessagePromptTemplate.from_template("{question}")

        # Combine prompts
        chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        # Initialize memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Initialize QA chain with memory
        self.qa = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"),
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 2}),
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": chat_prompt}
        )

    def query(self, question):
        result = self.qa.invoke({"question": question})
        return result["answer"]

def main():
    agent = SupportAgent()
    print("Customer Support Agent. Type 'exit' to quit.")
    while True:
        query = input("\nCustomer: ")
        if query.lower() == 'exit':
            break
        response = agent.query(query)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()