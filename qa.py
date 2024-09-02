
import config
import argparse

from langchain_community.chat_models import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain

import os
import helper
import prompts

os.environ["OPENAI_API_KEY"] = config.OPENAI_KEY


def get_answer(question):
    vectorDB = helper.load_persistent_db(
    "db"
    )
    llm = ChatOpenAI(model="gpt-4o-mini")
    prompt = prompts.load_prompt()

    question_answer_chain = create_stuff_documents_chain(llm, prompt)


    #Retrieval, Got top K chunks similar to question
    top_documents = helper.retrieve_documents(vectorDB,question,3)

    answer = question_answer_chain.invoke({"input": question,"context":top_documents})

    print("question asked: ", question)
    print("Answer by LLM: ", answer)
    #


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process PDF files from a directory.")
    parser.add_argument(
        '-q', '--question',
        type=str,
        default="What is multimodal information extraction?",
        help="Question to be asked"
    )

    args = parser.parse_args()
    get_answer(args.question)




