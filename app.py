from orchestration import MasterAgent

master = MasterAgent()

while True:

    task = input("User: ")

    result = master.run(task)

    print("\nRESULT:\n")
    print(result)