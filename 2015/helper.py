with open("input.txt", "r") as f:
    # Some description
    problem_data = f.read().strip() # type: str
with open("test1.txt", "r") as f:
    test_data = f.read().strip()
with open("test2.txt", "r") as f:
    example_data = f.read().strip()
    
    
def throw():
    raise Exception("Unreachable code detected")