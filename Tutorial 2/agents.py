from langchain import HuggingFaceHub
from langchain.agents import AgentType, initialize_agent, load_tools

huggingfacehub_llm = HuggingFaceHub(
    repo_id="google/flan-t5-large", model_kwargs={"temperature": 0.2, "max_length": 64})

tools = load_tools(["wikipedia", "llm-math"], llm=huggingfacehub_llm)

agent = initialize_agent(tools=tools, llm=huggingfacehub_llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True)

agent.run("When Was Elon Musk Born?")
