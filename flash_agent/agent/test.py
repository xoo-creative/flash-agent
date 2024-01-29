
import asyncio
from flash_agent.agent.async_agent import AsyncAgent


def test():
    a = AsyncAgent("Elm")

    result = asyncio.run(a.validate_technology("SOLID Principles"))
    print(result)

if __name__ == "__main__":
    test()