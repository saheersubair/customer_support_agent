# Customer Support AI Agent

This is a simple Customer Support AI Agent designed to answer common e-commerce questions using a Retrieval-Augmented Generation (RAG) approach. The agent retrieves relevant information from a knowledge base (product descriptions and company policies) and generates accurate, context-aware responses using OpenAI's LLM. It also includes memory for each session to maintain conversational context.

## Approach

1. **Knowledge Base**:
   - The agent uses two text files (`products.txt` and `policies.txt`) as its knowledge base.
   - These files contain product details (e.g., price, features, availability) and company policies (e.g., shipping, returns).

2. **Retrieval-Augmented Generation (RAG)**:
   - The agent uses ChromaDB for vector storage to efficiently retrieve relevant information from the knowledge base.
   - OpenAI's LLM generates responses based on the retrieved context.

3. **Memory**:
   - The agent uses `ConversationBufferMemory` to remember the conversation history within a session.
   - This allows the agent to handle follow-up questions and maintain context.

4. **Command-Line Interface**:
   - The agent is accessible via a simple command-line interface (CLI).

## Setup Instructions

1. **Install Python**:
   - Ensure Python 3.8 or later is installed on your system.

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate.bat  # Windows
   
3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   
4. **Setup OpenAI Key in .env File**
   ```bash
   OPENAI_API_KEY=your_api_key_here 

5. **Prepare Knowledge Base in knowledge_base Folder**

6. **Run the agent**
   ```bash
   python agent.py
   python3 agent.py
   
## Example Conversations
1. User: How much does the Ultraphone X cost?

   Agent: The UltraPhone X is priced at $799. If you have any other questions or need further assistance, feel free to ask!
2. User: Is it available in Red?

   Agent: I’m sorry, but the UltraPhone X is currently available in Black, Silver, and Blue only. Unfortunately, there is no Red option at this time. If you have any other questions or need further assistance, feel free to ask!
3. User: What are your shipping options?

   Agent: We offer two shipping options for your convenience:
   1. **Standard Shipping** (3-5 business days) for a fee of **$4.99**.
   2. **Express Shipping** (1-2 business days) for a fee of **$12.99**.
   Additionally, we provide **free standard shipping** on orders over **$50**. If you have any further questions or need assistance with your order, feel free to ask!

# Dependencies
Python 3.8

Libraries: langchain-openai, chromadb, python-dotenv, tiktoken, langchain, langchain_community"# customer_support_agent" 
