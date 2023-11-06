"""Example of Python client calling Knowledge Graph Search API."""

from llama_index import GPTListIndex, Document

import google_kg_helper

def kg_search(entity_name, *questions):
    ret = ""
    context_text = google_kg_helper.get_context_text(entity_name)
    print(f"Context text: {context_text}")
    doc = Document(text=context_text)
    index = GPTListIndex.from_documents([doc])
    for question in questions:
        response = index.as_query_engine().query(question)
        ret += f"QUESTION:  {question}\nRESPONSE: {response}\n"
    return ret

if __name__ == "__main__":
    print(kg_search("Anup Jadhav", "Is Anup a Salesforce Architect?"))
