use core::panic;
use std::{collections::HashMap, ops::Index, vec};

#[derive(Debug)]
struct LFUCache {
    // This is key: (value, count)
    cache: HashMap<i32, (i32, usize)>,
    counts: HashMap<usize, Vec<i32>>,
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
        println!("get {:?}", self.cache);
        match self.cache.get_mut(&key) {
            None => return -1,
            Some(value) => {
                value.1 += 1;
                return (*value).0;
            },
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
                return lowest_rank_array.remove(0);
            }
        }
    }
    fn bump_use_count(&mut self, key: i32) {
        let count = self.cache[&key].1;
        match self.counts.get_mut(&count) {
            None => (),
            Some(arr) => {
                arr.remove(*(arr.index(count)) as usize);
            }
        }
        match self.cache.get_mut(&key) {
            None => (),
            Some(arr) => {
                arr.1 += 1;
            }
        }
        if !self.counts.contains_key(&(count + 1)) {
            self.counts.insert(count + 1, vec![]);
        }
        match self.counts.get_mut(&(count + 1)) {
            None => (),
            Some(arr) => {
                arr.push(key);
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
                self.counts.insert(first_key, vec![key]);
                return;
            }
            Some(arr) => {
                arr.push(key);
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

    fn put(&mut self, key: i32, value: i32) {
        println!("put {:?}", self.cache);
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
