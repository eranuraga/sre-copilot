import asyncio

from agent import ask_agent, create_sre_agent, watch_agent


async def main():
  print("========================================\n 🤖 SRE Copilot v1 \n========================================")
  try:
    # Set up the model and Kubernetes tools once at startup.
    await create_sre_agent()
  except Exception as e:
    print("❌ Unable to initialize SRE Copilot.")
    print(e)
    return

  while True:
        mode = input("Mode [ask/watch] or type[exit/quit] to quit: ")
        if mode.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        question = input("SRE Copilot > ")
        try:
         if mode.lower() == "ask":
          response = await ask_agent(question)
          print(response)
         elif mode.lower() == "watch":
          await watch_agent(question)
         else:
          print("❌ Invalid mode. Choose 'ask' or 'watch'.")
        except Exception as e:
         print("❌ Failed to process request.")
         print(e)


if __name__ == "__main__":
    asyncio.run(main())
