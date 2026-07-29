use std::collections::VecDeque;

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut pointer: usize = 0;
        let mut negation: VecDeque<bool> = VecDeque::new();
        let mut is_negated: bool = false;
        let mut next_number_is_negated: bool = false;
        let mut total: i32 = 0;
        let input_string: Vec<char> = s.chars().collect();
        let n: usize = input_string.len();
        while pointer < n {
            match input_string[pointer] {
                ')' => {
                    if !negation.is_empty()
                        && !negation.pop_back().expect("Why would this go wrong")
                    {
                        is_negated = !is_negated;
                    }
                }
                '(' => {
                    negation.push_back(!next_number_is_negated);
                    if next_number_is_negated {
                        is_negated = !is_negated;
                    }
                    next_number_is_negated = false;
                }
                '-' => {
                    next_number_is_negated = true;
                }
                '+' | ' ' => {
                }
                _ => {
                    let start_pointer = pointer;
                    while pointer < n && input_string[pointer].is_numeric() {
                        pointer += 1;
                    }
                    total += input_string
                        .iter()
                        .skip(start_pointer)
                        .take_while(|x| x.is_numeric())
                        .enumerate()
                        .map(|(idx, &c)| {
                            ((10_u32).pow(((pointer - start_pointer) - idx - 1) as u32))
                                * c.to_digit(10).expect("Cast failed")
                        })
                        .sum::<u32>() as i32
                        * match is_negated ^ next_number_is_negated {
                            false => 1,
                            true => -1,
                        };
                    next_number_is_negated = false;
                    continue;
                }
            }
            pointer += 1;
        }
        return total;
    }
}
