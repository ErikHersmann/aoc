use core::panic;
use std::{
    collections::{HashMap, VecDeque},
    ops::Index,
    vec,
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
            cache: HashMap::new(),
            counts: HashMap::new(),
            capacity: capacity,
        };
    }

    fn get(&mut self, key: i32) -> i32 {
        self.debug(&format!("before get {}", &key.to_string()));
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
            None => panic!(),
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
            None => panic!("did not expect to be in here count: {}", count),
            Some(arr) => {
                println!("array in bump use count {:?} removing key {}", arr, key);
                arr.remove(
                    *(arr.iter().find(|&x| *x == key))
                        .expect(&format!("Expected to find {} in counts", key))
                        as usize,
                );
                println!("array in bump use count {:?} after removing key {}", arr, key);
            }
        }
        match self.cache.get_mut(&key) {
            None => (),
            Some(arr) => {
                arr.1 += 1;
            }
        }
        if !self.counts.contains_key(&(count + 1)) {
            self.counts.insert(count + 1, VecDeque::new());
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
            None => return,
            Some(value_and_count) => {
                value_and_count.0 = value;
                value_and_count.1 += 1;
                return;
            }
        }
    }

    fn insert_key(&mut self, key: i32, value: i32) {
        self.cache.insert(key, (value, 1));
        let first_key: usize = 1 as usize;
        match self.counts.get_mut(&first_key) {
            None => {
                self.counts
                    .insert(first_key, VecDeque::from_iter(vec![key]));
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
        println!("lfu key {}", lfu_key);
        self.cache.remove(&lfu_key);
        self.insert_key(key, value);
        return;
    }
    fn debug(&self, msg: &str) {
        println!("{} (cache){:?}", msg, self.cache);
        println!("{} (counts){:?}", msg, self.counts);
    }

    fn put(&mut self, key: i32, value: i32) {
        self.debug(&format!("before put {}", &key.to_string()));
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
