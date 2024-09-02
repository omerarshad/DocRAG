
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

import helper

import os

def load_persistent_db(persist_directory):
    # persist_directory = 'db'
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    collection_metadata = {"hnsw:space": "cosine"}
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings,
                      collection_metadata=collection_metadata)
    # print(vectordb._collection.count())

    return vectordb


def read_pdfs(directory):
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_files.extend(PyPDFLoader(directory + "/" + filename).load())


    return pdf_files

def retrieve_documents(vectorDB,question,topK):
    docs =vectorDB.similarity_search_with_score(question, k=topK)

    top_documents = []
    for doc in docs:
        top_documents.append(Document(page_content=doc[0].page_content))

    return top_documents


def ingest_pdfs(directory):
    pdf_files = helper.read_pdfs(directory)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150
    )
    splits = text_splitter.split_documents(pdf_files)

    persist_directory = 'db'
    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )

    vectordb.persist()
    print(print(vectordb._collection.count()))
    print("Successfully ingested {0} PDF files. DB stored at location: {1}".format(len(os.listdir(directory)),
                                                                                   persist_directory))
