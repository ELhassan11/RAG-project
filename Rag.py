import streamlit as st
import numpy as np
import faiss #facebook ai similarity search
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import PyPDFLoader
import tempfile
import google.generativeai as genai
api = os.getenv("GEMINI_API_KEY")
st.title('RAG Application Using Gemini AI')

#configure google generative ai
if api:
    genai.configure(api_key= api)
else:
    st.error('Your API is Not Valid')
#define a function for text generation
def Generate_Text(text):
    #call generative model('gemini-2.5-flash')
    model = genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content(text)
    return response.text

if 'message'not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    with st.chat_message(message['role']):
        st.markdown(message['content'])



#upload pdf file
upload_file = st.file_uploader('Choose PDF File...',type = ['pdf'])

if upload_file is not None:
    with tempfile.NamedTemporaryFile(delete=False,suffix='.pdf')as tempfile:
        tempfile.write(upload_file.read())
        tempfile_path = tempfile.name

    loader = PyPDFLoader(tempfile_path)
    documnets = loader.load()
    #st.write(documnets)
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    #create embedding
    text = [doc.page_content for doc in documnets]
    embeddings = embedding_model.encode(text,show_progress_bar=True)
    embedding_matrix = np.array(embeddings)

    #st.write(embedding_matrix)
    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)
    st.success('PDF Processed Successfuly')
    #USER input
    user_input= st.chat_input('Enter a Text to Search...')

    if user_input:
        with st.chat_message('user'):
            st.markdown(user_input)

        st.session_state.message.append({'role':'user','content': user_input})

        question_embedding = embedding_model.encode([user_input])

        k=1
        distances,indices = index.search(question_embedding,k)

        similar_doc = [documnets[i] for i in indices[0]]

        context = ""
        for i , doc in enumerate (similar_doc):
            context += doc.page_content + '\n'

        prompt = f'you are an assistant who retrieves answer based in the following content:{context}\n\nQuestion:{user_input}'

        response_text = Generate_Text(prompt)

        with st.chat_message('assistant'):
            message_placeholder = st.empty()
            with st.spinner('Generating Answer....'):
                response_text = Generate_Text(prompt)
                message_placeholder.markdown(f'{response_text}')
            st.session_state.message.append({'role':'assistant','content':response_text})
else:
    st.write('Please Upload a PDF File')
