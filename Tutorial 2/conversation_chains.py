from langchain import HuggingFaceHub
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

convo = ConversationChain(llm=HuggingFaceHub(
    repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.2, "max_length": 64}))
print(convo.prompt.template)

print(convo.run("What Is 5 + 5?"))
print(convo.run("Who Is Mayur Pai?"))
print(convo.memory)
print(convo.memory.buffer)

print("============================")

memory = ConversationBufferWindowMemory(k=1)
convo = ConversationChain(llm=HuggingFaceHub(
    repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.2, "max_length": 64}), memory=memory)
print(convo.prompt.template)

print(convo.run("What Is 12-3?"))
print(convo.memory)
print(convo.memory.buffer)
