from mapping_object import mapping_object
from lib import run_and_time
if __name__ == "__main__":
    
    sample = mapping_object(
        list(range(5)), lambda x: [0,2,1,2,0][x], "dp_test_medium"
    )
    run_and_time(sample.dynamic_programming_solve)

# "7%~x%3"