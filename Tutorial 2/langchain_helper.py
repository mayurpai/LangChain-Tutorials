from langchain import HuggingFaceHub
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate


def generate_restaurant_name_and_items(selected_cuisine):
    prompt_template_restaurant_name = PromptTemplate(input_variables=["cuisine"],
                                                     template="I Want To Open A Restaurant For {cuisine} Cuisine, Suggest Me A Fancy Name",
                                                     )

    llm_restaurant_chain = LLMChain(llm=HuggingFaceHub(
        repo_id="google/flan-t5-large",  model_kwargs={"temperature": 0, "max_length": 64}), prompt=prompt_template_restaurant_name, output_key="restaurant_name")

    prompt_template_name = PromptTemplate(input_variables=["restaurant_name"],
                                          template="Suggest Me Best Dishes In The Menu For {restaurant_name}",
                                          )

    llm_menu_items_chain = LLMChain(llm=HuggingFaceHub(
        repo_id="google/flan-t5-large",  model_kwargs={"temperature": 0, "max_length": 64}), prompt=prompt_template_name, output_key="menu_items")

    chain = SequentialChain(
        chains=[llm_restaurant_chain, llm_menu_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"])

    response = chain({"cuisine": selected_cuisine})
    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))
