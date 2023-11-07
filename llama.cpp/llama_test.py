from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Make sure the model path is correct for your system
llm = LlamaCpp(
    model_path="/Users/tesseract/01-10 Engineering/01 Software Development/01.11 Python/llama.cpp/models/openassistant-llama2-13b-orca-8k-3319.Q5_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True, # verbose for callback manager
)

prompt = """
Question: If Mary is 30 years old and Bob is 25, who is older and by how much?
"""
print(llm(prompt))
