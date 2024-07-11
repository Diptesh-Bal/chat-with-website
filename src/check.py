def get_vectorstore_from_url(url):
    # get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()
    
    # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    
    # Print the type of the first document chunk
    print("Type of document chunk:", type(document_chunks[0]))

    # Print all attributes and methods of the first document chunk
    print("Attributes and methods of document chunk:", dir(document_chunks[0]))
    
    # create a vectorstore from the chunks
    embeddings = cache_embeddings(document_chunks)
    vector_store = Chroma.from_embeddings(embeddings, document_chunks)

    return vector_store
