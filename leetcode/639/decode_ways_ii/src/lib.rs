impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        const MOD: u64 = 10_u64.pow(9) + 7;
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut prev: u64 = match chars[n - 1] {
            '*' => 9,
            '0' => 0,
            _ => 1,
        };
        let mut prev_prev: u64 = 1;
        for pointer in (0..n - 1).rev() {
            (prev_prev, prev) = (
                prev,
                (((match chars[pointer] {
                    '*' => 9,
                    '0' => 0,
                    _ => 1,
                }) * prev)
                    % MOD
                    + (match chars[pointer..pointer + 2] {
                        ['*', '*'] => 15,
                        ['1', '*'] => 9,
                        ['2', '*'] => 6,
                        ['*', '0']
                        | ['*', '1']
                        | ['*', '2']
                        | ['*', '3']
                        | ['*', '4']
                        | ['*', '5']
                        | ['*', '6'] => 2,
                        ['*', '7']
                        | ['*', '8']
                        | ['*', '9']
                        | ['1', '0']
                        | ['1', '1']
                        | ['1', '2']
                        | ['1', '3']
                        | ['1', '4']
                        | ['1', '5']
                        | ['1', '6']
                        | ['1', '7']
                        | ['1', '8']
                        | ['1', '9']
                        | ['2', '0']
                        | ['2', '1']
                        | ['2', '2']
                        | ['2', '3']
                        | ['2', '4']
                        | ['2', '5']
                        | ['2', '6'] => 1,
                        _ => 0,
                    } * prev_prev)
                        % MOD)
                    % MOD,
            )
        }
        return prev as i32;
    }
}
