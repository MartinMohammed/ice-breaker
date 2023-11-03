import os  # Importing the 'os' module to handle operating system related functionalities
from langchain.prompts import (
    PromptTemplate,
)  # Importing 'PromptTemplate' from a custom module
from langchain.chat_models import (
    ChatOpenAI,
)  # Importing 'ChatOpenAI' from a custom module
from langchain.chains import LLMChain  # Importing 'LLMChain' from a custom module
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup

# Input from the user asking for information about a product
information = """
Plantique Smart Indoor Garden
ab 649,00 €

Entdecke automatische und energieeffiziente Beleuchtung sowie Bewässerung, die optimal auf die Bedürfnisse deiner Pflanzen abgestimmt ist. Diese Lösung schont Ressourcen und bietet einen erheblichen Ertrag auf kleinstem Raum mit über 20 Pflanzplätzen.

Dank seiner kompakten Größe und modernen Gestaltung fügt sich Plantique perfekt in dein Zuhause ein.

Genieße nährstoffreichere und gesündere Ernten mit Anbau ohne Pestizide, direkt aus deinem eigenen Indoor-Garten.
"""

name = "Martin Mohammed"
company = "IBM"

# Only execute if this file was executed directly.
if __name__ == "__main__":
    # Fetches the OpenAI API key from the environment variables, providing a default message if not set
    OPENAI_API_KEY = os.environ.get(
        "OPENAI_API_KEY", "The environment variable 'OPENAI_API_KEY' is not set"
    )

    # The prompt template containing a placeholder {information}
    summary_template = """
    Given the LinkedIn information '{information}' about a person, I want you to create:
    1. a short summary
    2. two interesting facts about them
    And please make clear which response of you is related to which question:
    """

    # PromptTemplate contains variables and a template to create prompts
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # Setting up a language model to be used for generating responses
    # temperature parameter decides how creative the language model will be (0 implies less creativity)

    # gpt-3.5 token limit of 4k
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Chain setup: Using the ChatModel with the specified language model and prompt template
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_profile_url = lookup(name=name, company=company)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    # Running the chain using the user's provided information as a parameter
    print(chain.run(information=linkedin_data))

    # Now we can run this chain with different parameter values inside the prompt template.
