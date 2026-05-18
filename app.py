from orchestration import MasterAgent

master = MasterAgent()

print("=" * 60)
print("  Multi-Agent System — type 'exit' or 'quit' to stop")
print("=" * 60)

while True:
    try:
        task = input("\nUser: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        break

    if not task:
        continue

    if task.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    result = master.run(task)

    print("\n" + "=" * 60)
    print("RESULT:")
    print("=" * 60)
    print(result)