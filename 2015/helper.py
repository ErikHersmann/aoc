with open("input.txt", "r") as f:
    # Some description
    problem_data = f.read().strip() # type: str
    
def throw():
    raise Exception("Unreachable code detected")