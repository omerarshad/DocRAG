# DocRAG

Project Configurations:
In “config.py”, set your Openai api key as LLM used in the project is "gpt-4o-mini"
Prompt used to generate LLM response is in “prompts.py”

Embedding model used :
Currently, the project usts "all-MiniLM-L6-v2" as embedding model, which can be replaced with any Huggingface embedding Model. Refer to helper.py


Project contain 2 entry points:

- Data_ingestion.py:
It takes PDF files “directory” as input and ingests all data into Chroma DB
python3 data_ingestion.py --directory /path/to/pdf/folder

- qa.py
It takes a “question” as input and provides an answer based on ingested information.
python3 qa.py --q your question
