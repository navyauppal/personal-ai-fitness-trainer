from memory import InMemorySessionService
from agents import ControllerAgent

def main():
    print("Welcome to your personal AI Home Trainer!")
    name=input("What is your name: ")
    goal=input("What is your fitness goal? (weight loss/muscle gain/general): ")
    duration=input("How many minutes can you workout per day?: ")

    profile={
    "Name" : name,
    "Goal" : goal,
    "Duration": duration
    }

    session=InMemorySessionService()
    session.start_session(profile)

    print("\nSession Memory stored")
    print("Session profile: ",session.get_session_profile())

    controller=ControllerAgent(session)
    plan=controller.create_plan()

    print("\n============= PERSONAL TRAINER RESULT =============\n")
    print(plan)
    print("\n===================================================\n")


if __name__ == "__main__":
    main()

