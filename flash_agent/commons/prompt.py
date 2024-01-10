from enum import Enum, auto

class Prompt(Enum):
    CORE_APIS = "core_apis"
    CORE_CONCEPTS = "core_concepts"
    ONBOARDING = "onboarding"
    WITH_AND_WITHOUT = "with_and_without"
    SMALL_RUNNABLE_EXAMPLE = "small_runnable_example"
    REAL_LIFE_EXAMPLES = "real_life_examples"