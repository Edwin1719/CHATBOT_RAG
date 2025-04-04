# CHATBOT_RAG
## This code implements a Chatbot with Streamlit that acts as a virtual assistant for the company DATABiQ, being able to process PDF documents through a RAG technique (Retrieval Augmented Generation) to answer questions based on its knowledge base.

![Logo](https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt1496b19e4c6f9e66/66ba412a46b3f4241b969f48/rag-in-action.jpeg)

## Features

- **Importing necessary libraries:** The libraries required for the application's functionality are imported, including environment variable handling, PDF processing, OpenAI language models and embeddings, vector storage with FAISS, document and message handling, and the display of social media icons in Streamlit.
- **LLoading Environment Variables and API Keys:** Environment variables are loaded from an .env file and the OpenAI API key is obtained.
- **Inicialización de modelos de embeddings y lenguaje:** The OpenAI embedding model and GPT-4o language model are initialized with the provided API key.
- **Defining the function to process the PDF and create the vector store:**This function reads the content of the PDF specified in pdf_path, splits it into text fragments, and creates a list of Document objects. It then uses FAISS to create a vector store from these documents and the embedding model.
- **PDF processing and vector warehouse creation:** The existence of the PDF file at the specified path is verified. If it exists, it is processed and the vector store is created; otherwise, an error message is displayed in the application.
- **Initializing chat history:** The message history in the Streamlit session is initialized with a system message describing the assistant's role.
- **Viewing previous messages in the application:** The messages stored in the session are looped through and displayed in the chat interface, differentiating between messages from the user and the assistant.
- **Processing user input:** User input is expected via a text field. Once entered, it is added to the message history and displayed in the interface.
- **Recovery of relevant documents:** A retriever is configured that uses the vector store to find the documents most similar to the user's query, retrieving the 3 most relevant ones.
- **Determining the context for the response:** A system prompt is generated that guides the language model in generating the response, using the retrieved context or, failing that, its general knowledge.
- **Getting and displaying the language model response:** The language model is invoked with the message history to generate a response, which is then added to the history and displayed in the interface.
- **Footer with developer information and social media links:** Generation of the footer with all the information about the developer and their social networks.


## Technologies used

- **Streamlit:** An open-source Python framework that transforms data scripts into shareable web applications. In your script, it manages the user interface, displaying the chatbot and handling user interactions. ​
- **python-dotenv:** This library reads key-value pairs from a .env file and sets them as environment variables. It's used to load configuration settings, such as API keys, without hardcoding them into your script, enhancing security and flexibility.
- **PyPDF2:** A pure-Python library capable of splitting, merging, cropping, and transforming PDF files. In your script, it's employed to extract text from PDF documents, facilitating the processing of their content.
- **OpenAIEmbeddings (from langchain_openai):** Integrates OpenAI's embedding models into your application. It's used to convert text into numerical representations (embeddings), which are essential for tasks like semantic search and similarity comparisons.
- **ChatOpenAI (from langchain_openai):** Provides access to OpenAI's chat models, enabling the generation of human-like conversational responses. In your script, it's utilized to create an AI chatbot that interacts with users.
- **FAISS (from langchain_community.vectorstores):** Facebook AI Similarity Search (FAISS) is a library for efficient similarity search and clustering of dense vectors. In your application, it's used to store and retrieve document embeddings, facilitating quick similarity searches.
- **Document (from langchain_core.documents):** A class for storing pieces of text along with associated metadata. It's used to encapsulate text fragments extracted from PDFs, preparing them for embedding and storage.
- **HumanMessage, SystemMessage, AIMessage (from langchain_core.messages):** These classes represent different types of messages in a conversational context. HumanMessage denotes user inputs, SystemMessage is used for system-level instructions or context, and AIMessage represents responses from the AI model. They structure the dialogue flow within your chatbot. 
- **st-social-media-links:** A Streamlit component that displays social media icons with links. In your script, it's used to render social media links in the application's footer, enhancing user engagement. 

## **Documentation**
! https://datos.gob.es/es/blog/tecnicas-rag-como-funcionan-y-ejemplos-de-casos-de-uso
! https://www.youtube.com/watch?v=Mg3xOWWaF0c
