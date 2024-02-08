import os

from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

memory = ConversationBufferMemory()

huggingfacehub_llm = HuggingFaceHub(
    repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.2, "max_length": 64})

prompt_template_restaurant_name = PromptTemplate(input_variables=["cuisine"],
                                                 template="I Want To Open A Restaurant For {cuisine} Cuisine, Suggest Me A Fancy Name",
                                                 )

llm_restaurant_chain = LLMChain(
    llm=huggingfacehub_llm, prompt=prompt_template_restaurant_name, output_key="restaurant_name", memory=memory)

llm_restaurant_chain.run("Indian")

print(llm_restaurant_chain.memory.buffer)
