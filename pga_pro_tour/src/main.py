from mapping_object import mapping_object
from lib import run_and_time
if __name__ == "__main__":
    
    sample = mapping_object(
        list(range(5)), lambda x: [5,5,0,5,5][x], "dp_parenthesis_test_3"
    )
    run_and_time(sample.dynamic_programming_solve, [True])

# "7%~x%3"
# TODO: Save lower and upper bound on mapping_object
# TODO: Implement heuristics and update upper bound with those
# TODO: Multithreading support in main
# 5*(x>1)

# TODO: DP early stopping
# TODO: make this a ctor argument: early_stop: bool
# TODO: better next char: valid but pointless chars such as 03 or +3