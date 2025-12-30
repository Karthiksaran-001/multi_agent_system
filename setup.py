from setuptools import setup  , find_packages

setup(
    name = "research_analysis",
    author= "Karthik Saran",
    version="0.0.1",
    description="Mulyti-agent system for research analysis using LLMs",
    packages= find_packages(),
    install_requires =[
    "langchain",
    "langchain-community",
    "langchain-core",
    "langchain-groq",
    "langchain-google-genai",
    "langchain-astradb",
    "ragas",
    "astrapy",
    "langchain-astradb",
    "fastapi",
    "uvicorn",
    "python-dotenv",
    "python-multipart",
    "PyMuPDF",
    "structlog",
    "docx2txt",
    "ipykernel",
    "streamlit",
    "pytest",
])