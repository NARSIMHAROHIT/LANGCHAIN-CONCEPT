Architecture of RAG 
    Load [DATA INGESTION]     --------> 
    SPLIT DATA{Chunk DATA}(Data Transformation) --------> 
    EMBED DATA {we text embedding and conver into vector  so we     apply     similarity search like cosine similarity }-->
    STORE DATA {we store data in the vector store data bases like FIASS  Chromadb }

    We chunk data because the llm has limitation of context window  so we divided data into chunks
https://docs.langchain.com/oss/python/integrations/providers/overview
 Building an AI Chatbot
Project Objective
This project focuses on building an LLM-powered conversational chatbot that can:
Maintain conversation context
Remember previous messages
Respond intelligently using an LLM
Note:
This chatbot is designed to remember conversation history only.
It does not use external data retrieval by default.

Key Concepts Covered
Conversational Memory

Stores chat history

Enables contextual follow-up questions

Makes interactions feel natural

📚 Conversational RAG (Advanced)

Extends chatbot memory with external knowledge sources

Combines chat history + retrieved documents

 Agents

Agents can:

Decide what action to take

Call tools

Query databases

Execute tasks dynamically

This project introduces the foundation, with scope to extend into Agent-based architectures.

🔗 Useful References

LangChain Provider Integrations
https://docs.langchain.com/oss/python/integrations/providers/overview

🚀 Future Enhancements
Add Conversational RAG
Integrate external APIs
Tool-calling agents
Multi-document retrieval
Streaming responses
Memory optimization

