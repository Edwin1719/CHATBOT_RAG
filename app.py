import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from st_social_media_links import SocialMediaIcons

# Cargar variables de entorno y claves de API
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Inicializar modelos de embeddings y lenguaje
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=openai_api_key)
llm = ChatOpenAI(model="gpt-4o", temperature=1, api_key=openai_api_key)

# Función para procesar el PDF y crear el almacén de vectores
def procesar_pdf(pdf_path):
    texto = "".join(PdfReader(pdf_path).pages[i].extract_text() for i in range(len(PdfReader(pdf_path).pages)))
    fragmentos = [texto[i:i+1000] for i in range(0, len(texto), 800)]
    documentos = [Document(page_content=frag) for frag in fragmentos]
    return FAISS.from_documents(documentos, embeddings_model)

# Interfaz de usuario con Streamlit
st.title("Asistente Virtual DATABiQ")

# Procesar el PDF y crear el almacén de vectores
pdf_path = "RAG_CHATBOT/Perfil_DATABiQ.pdf"
if os.path.exists(pdf_path):
    vector_store = procesar_pdf(pdf_path)
else:
    st.error(f"No se encontró el archivo PDF en la ruta: {pdf_path}")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage("Asistente para tareas de atención al cliente con conocimientos en Ciencia de Datos.")]

# Mostrar mensajes del historial en la aplicación
for message in st.session_state.messages:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
        st.markdown(message.content)

# Procesar la entrada del usuario
if prompt := st.chat_input("¿En qué puedo ayudarte hoy?"):
    st.session_state.messages.append(HumanMessage(prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Recuperar documentos relevantes
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    docs = retriever.invoke(prompt)

    # Determinar el contexto para la respuesta
    if docs:
        contexto = " ".join(doc.page_content for doc in docs)
        system_prompt = f"""Eres un asistente para tareas de atención al cliente de DATABiQ.COM con conocimientos en ciencia de datos.
        Utiliza las siguientes piezas de contexto recuperado para responder la pregunta.
        Si no conoces la respuesta basándote en el contexto proporcionado, utiliza tu conocimiento general.
        Usa un máximo de tres oraciones y mantén la respuesta concisa.
        Contexto: {contexto}"""
    else:
        system_prompt = f"""Eres un asistente para tareas de atención al cliente con conocimientos en ciencia de datos.
        Responde la pregunta utilizando tu conocimiento general.
        Usa un máximo de tres oraciones y mantén la respuesta concisa."""

    # Añadir el mensaje del sistema al historial
    st.session_state.messages.append(SystemMessage(system_prompt))

    # Obtener y mostrar la respuesta del modelo de lenguaje
    respuesta = llm.invoke(st.session_state.messages).content
    st.session_state.messages.append(AIMessage(respuesta))
    with st.chat_message("assistant"):
        st.markdown(respuesta)

# Pie de página con información del desarrollador y logos de redes sociales
st.markdown("""
---
**Desarrollador:** Edwin Quintero Alzate/
**Email:** egqa1975@gmail.com
""")

social_media_links = [
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()