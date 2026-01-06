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

Enter the query hi this is rohit how are you 
AI Response = content="Hello Rohit, I'm doing well, thank you for asking. I'm a large language model, so I don't have feelings or emotions like humans do, but I'm functioning properly and ready to help with any questions or topics you'd like to discuss. How can I assist you today?" additional_kwargs={} response_metadata={'token_usage': {'completion_tokens': 61, 'prompt_tokens': 44, 'total_tokens': 105, 'completion_time': 0.081119108, 'completion_tokens_details': None, 'prompt_time': 0.00213121, 'prompt_tokens_details': None, 'queue_time': 0.010571677, 'total_time': 0.083250318}, 'model_name': 'llama-3.1-8b-instant', 'system_fingerprint': 'fp_9ca2574dca', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'} id='lc_run--019b94c6-702b-77a3-b7b9-80beb50f092e-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 44, 'output_tokens': 61, 'total_tokens': 105}



python ./src/chatbot.py
Enter the queryhi this is rohit 
AI Response = Hi Rohit, how are you doing today? Is there something I can help you with or would you like to chat?
