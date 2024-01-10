from dotenv import load_dotenv
from flash_agent.commons.utils import _write_flash, load_prompt
from flash_agent.commons.learning_material import LearningMaterial
from flash_agent.commons.prompt import Prompt
import asyncio
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

import logging

class AsyncAgent:

    def __init__(self, technology: str, gpt_version: str = "gpt-3.5-turbo") -> None:
        """
        Initializes an Agent object.

        Parameters:
            technology (str): The name of the technology for the Agent.
              
        Optional:
            gpt_version (str): Specifies the version of OpenAI GPT you want.

        Returns:
            None
        """
        
        self.technology: str = technology
        self.learning_material: LearningMaterial = LearningMaterial(technology=technology)
        self.openai_chat = ChatOpenAI(temperature=0, model=gpt_version)

    async def write_section(self, section: Prompt, technology_name: str) -> str:
        """
        Writes a section of the learning material, asynchronously.

        Parameters:
            section (Prompt): The section prompt to guide the content.
            technology_name (str): The name of the technology for the section.
        """
        requested_prompt = load_prompt(section)
        
        if technology_name == "":
            raise RuntimeError("No technology name is provided, but it is required.")

        human_prompt_template = "{technology_name}"

        system_message_prompt = SystemMessagePromptTemplate.from_template(requested_prompt)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_prompt_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chat_response = await self.openai_chat.ainvoke(
            chat_prompt.format_prompt(
                technology_name=technology_name
            ).to_messages()
        )

        return chat_response.content
    
    async def generate_section(self, section_title: Prompt) -> str:
        """
        Generates a section of the learning material.

        Parameters:
            section_title (Prompt): The title prompt of the section.

        Returns:
            str: The content of the generated section.
        """
        logging.info(f"Writing {section_title.value} section.")

        section_content = await self.write_section(section_title, self.technology)
        self.learning_material.set(section_title, section_content)

        logging.info(f"Finished writing {section_title.value} section.")

        return section_content
    
    async def generate_full_async(self) -> str:
        """
        Generates the full learning material and returns it as a string, asynchronously

        Parameters:
            None
        """
        results = await asyncio.gather(
            self.generate_section(Prompt.ONBOARDING),
            self.generate_section(Prompt.WITH_AND_WITHOUT),
            self.generate_section(Prompt.CORE_CONCEPTS),
            self.generate_section(Prompt.CORE_APIS),
            self.generate_section(Prompt.SMALL_RUNNABLE_EXAMPLE)
        )

        material = self.learning_material.render()

        # self.to_md(material)

        return material
    
    def to_md(self, content: str = "", filename: str = "content.md") -> None:
        """
        Writes a string to a local markdown file to folder <project_root>/flash/text_examples/

        Default behaviour writes the current `self.learning_material` to `text_examples/content.md`.
        """
        if content == "":
            content = self.learning_material.render()

        _write_flash(content, f"text-examples/{filename}")

        
    





