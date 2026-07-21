import asyncio

from agent import ask_agent, create_sre_agent


async def main():
    # Set up the model and Kubernetes tools once at startup.
    await create_sre_agent()

    while True:
        question = input("SRE Copilot > ")
        response = await ask_agent(question)
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
