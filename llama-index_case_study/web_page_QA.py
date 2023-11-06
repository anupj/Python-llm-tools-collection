from pprint import pprint
from llama_index import GPTListIndex
from llama_index import TrafilaturaWebReader

def query_website(url_list, *questions):
    documents = TrafilaturaWebReader().load_data(url_list)
    print("documents:"); pprint(documents)
    index = GPTListIndex.from_documents(documents)
    engine = index.as_query_engine()
    for question in questions:
        print(f"\n== QUESTION: {question}\n")
        response = engine.query(question)
        print(f"== RESPONSE: {response}")

if __name__ == "__main__":
    url_list = ["https://www.anup.io/p/invert-always-invert"]
    query_website(url_list, "Describe the principle mentioned here?", 
                  "summarise this post in less than 4 sentences?")

