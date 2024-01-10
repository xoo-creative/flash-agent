
from dataclasses import dataclass

from flash_agent.commons.prompt import Prompt


@dataclass
class LearningMaterial:
    technology: str
    onboarding: str = None
    with_and_without: str = None
    core_concepts: str = None
    core_apis: str = None
    small_runnable_example: str = None
    real_life_examples: str = None

    def get(self, prompt: Prompt) -> str:
        return getattr(self, prompt.value)
    
    def set(self, prompt: Prompt, val: str) -> None:
        return setattr(self, prompt.value, val)
    
    def title(self) -> str:
        return f"# {self.technology.capitalize()}"
    
    def render(self) -> str:

        sections_to_include = []

        if self.onboarding:
            sections_to_include.append(self.onboarding)
        
        if self.with_and_without:
            sections_to_include.append(self.with_and_without)

        if self.core_concepts:
            sections_to_include.append(self.core_concepts)

        if self.core_apis:
            sections_to_include.append(self.core_apis)

        if self.small_runnable_example:
            sections_to_include.append(self.small_runnable_example)
        
        if self.real_life_examples:
            sections_to_include.append(self.real_life_examples)

        if len(sections_to_include) > 0:
            sections_to_include.insert(0, self.title())

        return "\n \n".join(sections_to_include)