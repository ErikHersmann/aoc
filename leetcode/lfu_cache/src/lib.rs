use std::{
    collections::{HashMap, VecDeque},
};

#[derive(Debug)]
struct LFUCache {
    // This is key: (value, count)
    cache: HashMap<i32, (i32, usize)>,
    counts: HashMap<usize, VecDeque<i32>>,
    capacity: i32,
}

impl LFUCache {
    fn new(capacity: i32) -> Self {
        return LFUCache {
            cache: HashMap::with_capacity( capacity as usize),
            counts: HashMap::new(),
            capacity: capacity,
        };
    }

    fn get(&mut self, key: i32) -> i32 {
        match self.cache.get(&key).cloned() {
            Some(value) => {
                self.bump_use_count(key);
                return value.0;
            }
            None => return -1,
        }
    }

    fn get_lfu_key(&mut self) -> i32 {
        let mut rank = 1 as usize;
        loop {
            match self.counts.get(&rank) {
                None => continue,
                Some(arr) => {
                    if arr.len() > 0 {
                        break;
                    }
                }
            }
            rank += 1;
        }

        match self.counts.get_mut(&rank) {
            None => -1,
            Some(lowest_rank_array) => {
                return lowest_rank_array
                    .pop_front()
                    .expect("Could not pop from an array");
            }
        }
    }
    fn bump_use_count(&mut self, key: i32) {
        let count = self.cache[&key].1;
        match self.counts.get_mut(&count) {
            None => (),
            Some(arr) => {
                for (index, index_value) in arr.iter().enumerate() {
                    if index_value == &key {
                        arr.remove(index);
                        break;
                    }
                }
            }
        }
        match self.cache.get_mut(&key) {
            None => (),
            Some(arr) => {
                arr.1 += 1;
            }
        }
        if !self.counts.contains_key(&(count + 1)) {
            self.counts.insert(count + 1, VecDeque::with_capacity(150));
        }
        match self.counts.get_mut(&(count + 1)) {
            None => (),
            Some(arr) => {
                arr.push_back(key);
            }
        }
    }

    fn update_key(&mut self, key: i32, value: i32) {
        match self.cache.get_mut(&key) {
            None => (),
            Some(value_and_count) => {
                value_and_count.0 = value;
            }
        }
        self.bump_use_count(key);
    }

    fn insert_key(&mut self, key: i32, value: i32) {
        self.cache.insert(key, (value, 1));
        let first_key: usize = 1 as usize;
        match self.counts.get_mut(&first_key) {
            None => {
                let mut dq : VecDeque<i32> = VecDeque::with_capacity(150);
                dq.push_back(key);
                self.counts
                    .insert(first_key, dq);
                return;
            }
            Some(arr) => {
                arr.push_back(key);
                return;
            }
        }
    }

    fn replace_key(&mut self, key: i32, value: i32) {
        let lfu_key: i32 = self.get_lfu_key();
        self.cache.remove(&lfu_key);
        self.insert_key(key, value);
    }

    fn put(&mut self, key: i32, value: i32) {
        if self.cache.contains_key(&key) {
            self.update_key(key, value);
            return;
        }
        if self.cache.len() < (self.capacity as usize) {
            self.insert_key(key, value);
            return;
        }
        self.replace_key(key, value);
    }
}
