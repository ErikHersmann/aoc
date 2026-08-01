use std::collections::HashMap;

impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        const MOD: u64 = 10_u64.pow(9) + 7;
        let map: HashMap<String, u64> = Self::get_hash_map();
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut prev: u64 = 1;
        let mut prev_prev: u64 = 0;
        for pointer in (0..n).rev() {
            (prev_prev, prev) = (
                prev,
                ((map[&chars[pointer].to_string()] * prev) % MOD
                    + ((match pointer < n - 1 {
                        true => map[&chars[pointer..pointer + 2].iter().collect::<String>()],
                        false => 0,
                    }) * prev_prev)
                        % MOD)
                    % MOD,
            )
        }
        return prev as i32;
    }

    fn get_hash_map() -> HashMap<String, u64> {
        // TODO: This is known at compile time
        let mut temp: HashMap<String, u64> = HashMap::with_capacity(110);
        for number in 1..27 {
            temp.insert(number.to_string(), 1);
        }
        temp.insert("0".to_string(), 0);
        temp.insert("0*".to_string(), 0);
        for number in 27..100 {
            temp.insert(number.to_string(), 0);
        }
        for number in 0..10 {
            temp.insert(format!("0{}", number), 0);
        }
        for number in 3..10 {
            temp.insert(format!("{}*", number), 0);
        }
        temp.insert("*".to_string(), 9);
        temp.insert("**".to_string(), 15);
        temp.insert("1*".to_string(), 9);
        temp.insert("2*".to_string(), 6);
        temp.insert("*0".to_string(), 2);
        temp.insert("*1".to_string(), 2);
        temp.insert("*2".to_string(), 2);
        temp.insert("*3".to_string(), 2);
        temp.insert("*4".to_string(), 2);
        temp.insert("*5".to_string(), 2);
        temp.insert("*6".to_string(), 2);
        temp.insert("*7".to_string(), 1);
        temp.insert("*8".to_string(), 1);
        temp.insert("*9".to_string(), 1);
        return temp;
    }
}
