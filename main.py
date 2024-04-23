from langchain_community.document_loaders import UnstructuredFileLoader

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

new_db = FAISS.load_local("faiss_index", embeddings)

# query = "What did the president say about Ketanji Brown Jackson"
# docs = new_db.similarity_search(query)

# print(docs[0].page_content)

cpu_llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    device=-1,  # replace with device_map="auto" to use the accelerate library.
    pipeline_kwargs={"max_new_tokens": 10},
)

def response_generator(question):

    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | cpu_llm

    question = "What is electroencephalography?"

    return(chain.invoke({"question": question}))
