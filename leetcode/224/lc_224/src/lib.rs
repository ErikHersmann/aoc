use std::collections::VecDeque;

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut pointer: usize = 0;
        let mut negation: VecDeque<bool> = VecDeque::new();
        let mut is_negated: bool = false;
        let mut next_number_is_negated: bool = false;
        let mut total: i32 = 0;
        let input_string: Vec<char> = s.chars().collect();
        let n = input_string.len();
        while pointer < n {
            match input_string[pointer] {
                ')' => {
                    if !negation.is_empty()
                        && !negation.pop_back().expect("Why would this go wrong")
                    {
                        is_negated = !is_negated;
                    }
                    pointer += 1;
                }
                '(' => {
                    if next_number_is_negated {
                        negation.push_back(false);
                        is_negated = !is_negated;
                        next_number_is_negated = false;
                    } else {
                        negation.push_back(true);
                    }
                    pointer += 1;
                }
                '+' | ' ' => {
                    pointer += 1;
                }
                '-' => {
                    next_number_is_negated = true;
                    pointer += 1;
                }
                _ => {
                    let mut temp: Vec<char> = vec![];
                    while pointer < n && input_string[pointer].is_numeric() {
                        temp.push(input_string[pointer]);
                        pointer += 1;
                    }
                    let num: usize = temp
                        .iter()
                        .enumerate()
                        .map(|(idx, &c)| {
                            ((10 as usize).pow((temp.len() - idx - 1) as u32))
                                * (c.to_digit(10).expect("Cast failed") as usize)
                        })
                        .sum();
                    // println!("{:?},numeric: {}", temp, num);
                    if is_negated ^ next_number_is_negated {
                        total -= num as i32;
                    } else {
                        total += num as i32;
                    }
                    next_number_is_negated = false;
                    continue;
                }
            }
        }
        return total;
    }
}
