import os
import requests
import streamlit as st
from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from st_social_media_links import SocialMediaIcons

# Acceder a la clave de API desde st.secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Inicializar modelos de embeddings y lenguaje
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=openai_api_key)
llm = ChatOpenAI(model="gpt-4o", temperature=1, api_key=openai_api_key)

# Función para procesar el PDF y crear el almacén de vectores
def procesar_pdf(pdf_path):
    texto = "".join(PdfReader(pdf_path).pages[i].extract_text() for i in range(len(PdfReader(pdf_path).pages)))
    fragmentos = [texto[i:i+1000] for i in range(0, len(texto), 800)]
    documentos = [Document(page_content=frag) for frag in fragmentos]
    return FAISS.from_documents(documentos, embeddings_model)

# URL de la imagen
imagen_url = "https://www.valuetech.cl/wp-content/uploads/2022/08/Portadas-Contenidos-Sitio-8.png"

# Mostrar la imagen encima del título
st.image(imagen_url, use_container_width=True)

# Agregar el logo en la parte superior izquierda
st.markdown(
    """<style>.header-container {display: flex;align-items: center;}
    .header-container img {margin-right: 20px;}
    .header-container h1, .header-container p {text-align: center;flex: 1;}
    </style>
    """,unsafe_allow_html=True)

# Encabezado de la Aplicacion de Streamlit con logo
st.markdown(
    """
    <div class="header-container">
        <img src="https://cdn-icons-gif.flaticon.com/17576/17576923.gif" width="50" height="50">
        <div>
            <h1>ChatBot DATABiQ</h1>
        </div>
    </div>
    """,unsafe_allow_html=True)

# Procesar el PDF y crear el almacén de vectores
pdf_path = "Perfil_DATABiQ.pdf"
if os.path.exists(pdf_path):
    vector_store = procesar_pdf(pdf_path)
else:
    st.error(f"No se encontró el archivo PDF en la ruta: {pdf_path}")

# Inicializar historial de chat (sin mensajes de sistema repetitivos)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos en la interfaz
for message in st.session_state.messages:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
        st.markdown(message.content)

# Procesar la entrada del usuario
if prompt := st.chat_input("¿En qué puedo ayudarte hoy?"):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Recuperar documentos relevantes
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    docs = retriever.invoke(prompt)
    contexto = " ".join(doc.page_content for doc in docs) if docs else ""

    # Construir mensaje del sistema para esta sola consulta (sin guardarlo en el historial)
    system_prompt = (
        f"Eres un asistente para tareas de atención al cliente de DATABiQ.COM con conocimientos en ciencia de datos. "
        f"Utiliza las siguientes piezas de contexto recuperado para responder la pregunta. "
        f"Si no conoces la respuesta basándote en el contexto proporcionado, utiliza tu conocimiento general. "
        f"Usa un máximo de tres oraciones y mantén la respuesta concisa. "
        f"Contexto: {contexto}" if contexto else
        f"Eres un asistente para tareas de atención al cliente con conocimientos en ciencia de datos. "
        f"Responde utilizando tu conocimiento general. "
        f"Usa un máximo de tres oraciones y mantén la respuesta concisa."
    )

    # Crear una copia temporal del historial con el nuevo system prompt
    mensajes_para_llm = [SystemMessage(content=system_prompt)] + st.session_state.messages

    # Obtener respuesta del modelo
    respuesta = llm.invoke(mensajes_para_llm).content

    # Mostrar y guardar respuesta
    st.session_state.messages.append(AIMessage(content=respuesta))
    with st.chat_message("assistant"):
        st.markdown(respuesta)

# Pie de página
st.markdown("""
---
**Desarrollador:** Edwin Quintero Alzate  
**Email:** egqa1975@gmail.com
""")

social_media_links = [
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"
]
social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()
