from mapping_object import mapping_object

if __name__ == "__main__":
    sample = mapping_object(
        list(range(5)), lambda x: 0 if x != 3 else 1, "pydle 188 y=0"
    )
    sample.solve()
    sample = mapping_object(
        list(range(5)), lambda x: 1 if x in [3,4] else (0 if x == 0 else 2), "pydle 188 y=1"
    )
    sample.solve()
    sample = mapping_object(
        list(range(5)), lambda x: 2*(x%4>0), "pydle 188 y=2"
    )
    sample.solve()
    sample = mapping_object(
        list(range(5)), lambda x: (x<4)*(1+x//2), "pydle 188 y=3"
    )
    sample.solve()
    sample = mapping_object(
        list(range(5)), lambda x: 1 if x ==1 else 0, "pydle 188 y=4"
    )
    
    sample.solve()