# RAG PIPELINE DOCUMENT
## Importing the questions:
- these questions are made via chatgpt.
- these are the most frequesntly asked questions.
```python
from langchain_community.document_loaders.csv_loader import CSVLoader
# enter file path
loader_csv = CSVLoader(file_path="") 
data=loader_csv.load()
```
## TEXT spliting For large Dataset
- used langchain recursive character text splitter.
- This is done for larger data set, not required for this project.
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
#splitting the text into
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(data)
```
## Embedding
- Used Langchain embedding to import huggingfacebgeembeddings.
- Huggingfacebgeembedding used to embed the TEXT.
```python
from langchain.embeddings import HuggingFaceBgeEmbeddings

model_name = "BAAI/bge-base-en"
encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

bge_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs={'device': 'cpu'},
    encode_kwargs=encode_kwargs
)
```
## Creating Vector Database
- used langcchain and chroma libraries to create vector database
- used for getting the simlarity search and retreival in rag pipeline
```python
from langchain_chroma import Chroma

persist_directory = 'db'

## Here you can change the embeddings etc
embedding = bge_embeddings

vectordb = Chroma.from_documents(documents=texts,
                                 embedding=embedding,
                                 persist_directory=persist_directory)
```
## Creating retriever
```python
retriever = vectordb.as_retriever(search_kwargs={"k": 5})
```
## IMporting Libraries and Model
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

from langchain_groq import ChatGroq

GROQ_LLM = ChatGroq(
            model="llama3-70b-8192",
        )
```
## Creating RAG propmt Template
```python
#RAG Chain
rag_prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\n

     <|eot_id|><|start_header_id|>user<|end_header_id|>
    QUESTION: {question} \n
    CONTEXT: {context} \n
    Answer:
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=["question","context"],
)
```
## Creating RAG Chain
```python
rag_chain = (
    {"context": retriever , "question": RunnablePassthrough()}
    | rag_prompt
    | GROQ_LLM
    | StrOutputParser()
)
```
## Method to Run Chain
```python
rag_chain.invoke(question)
```
