Architecture of RAG 
    Load [DATA INGESTION]     --------> 
    SPLIT DATA{Chunk DATA}(Data Transformation) --------> 
    EMBED DATA {we text embedding and conver into vector  so we     apply     similarity search like cosine similarity }-->
    STORE DATA {we store data in the vector store data bases like FIASS  Chromadb }

    We chunk data because the llm has limitation of context window  so we divided data into chunks
