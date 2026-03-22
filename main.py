from dotenv import load_dotenv
from crew import RemoteWorkIranCrisisCrew

load_dotenv()

# Initialize the crew

def run():
    result = RemoteWorkIranCrisisCrew().crew().kickoff()
    print(result)

if __name__ == "__main__":
    run()