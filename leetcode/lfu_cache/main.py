class LFUCache:
    """Should not remove and add to list maybe for use_counts
   
    Dequeue with all values ever: giving u the order of least recently used
    going from the end there u compare to ur current_global_lowest_count u keep track of (by keeping use_count: number of keys at that count tracker)
    """
    def __init__(self, capacity: int):
        self.CAPACITY = capacity
        self.value_cache = {}
        self.count_cache = {}
        self.sorted_counts = {1: []}

    def get_lfu_key(self) -> int:
        """Gets the oldest key with the lowest usecount. Where key age is the tie breaker"""
        rank = 1
        while len(self.sorted_counts[rank]) == 0:
            rank += 1
        return self.sorted_counts[rank].pop(0)

    def get(self, key: int) -> int:
        if key not in self.value_cache:
            return -1
        self.bump_use_count(key)
        return self.value_cache[key]

    def bump_use_count(self, key) -> None:
        count = self.count_cache[key]
        self.sorted_counts[count].remove(key)
        self.count_cache[key] += 1
        if count+1 not in self.sorted_counts:
            self.sorted_counts[count+1] = []
        self.sorted_counts[count+1].append(key)

    def update_key(self, key, value) -> None:
        self.value_cache[key] = value
        self.bump_use_count(key)

    def insert_key(self, key, value) -> None:
        """Add a new key value pair"""
        self.value_cache[key] = value
        self.count_cache[key] = 1
        self.sorted_counts[1].append(key)

    def replace_key(self, key, value) -> None:
        """Remove the least frequently used key and add a new key"""
        lfu_key = self.get_lfu_key()
        self.value_cache.pop(lfu_key)
        self.count_cache.pop(lfu_key)
        self.insert_key(key, value)

    def put(self, key: int, value: int) -> None:
        if key in self.value_cache:
            self.update_key(key, value)
            return
        if len(self.value_cache) < self.CAPACITY:
            self.insert_key(key, value)
            return
        self.replace_key(key, value)


