from langchain_community.document_loaders import UnstructuredFileLoader

from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.prompts import PromptTemplate



loader = UnstructuredFileLoader("/home/harsh/Documents/langchain/book_companion/Indian Polity by M Laxmikanth.pdf")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# embeddings = OpenAIEmbeddings()
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embeddings)

db.save_local("faiss_index")