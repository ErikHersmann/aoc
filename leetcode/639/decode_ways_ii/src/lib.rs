impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        const MOD: u64 = 10_u64.pow(9) + 7;
        let bytes: Vec<u8> = s.into_bytes();
        let n = bytes.len();
        let mut prev: u64 = match bytes[n - 1] {
            b'*' => 9,
            b'0' => 0,
            _ => 1,
        };
        let mut prev_prev: u64 = 1;
        for pointer in (0..n - 1).rev() {
            (prev_prev, prev) = (
                prev,
                (((match bytes[pointer] {
                    b'*' => 9,
                    b'0' => 0,
                    _ => 1,
                }) * prev)
                    % MOD
                    + (match bytes[pointer..pointer + 2] {
                          [b'*', b'*'] => 15,
                          [b'1', b'*'] => 9,
                          [b'2', b'*'] => 6,
                          [b'*', b'0']
                        | [b'*', b'1']
                        | [b'*', b'2']
                        | [b'*', b'3']
                        | [b'*', b'4']
                        | [b'*', b'5']
                        | [b'*', b'6'] => 2,
                          [b'*', b'7']
                        | [b'*', b'8']
                        | [b'*', b'9']
                        | [b'1', b'0']
                        | [b'1', b'1']
                        | [b'1', b'2']
                        | [b'1', b'3']
                        | [b'1', b'4']
                        | [b'1', b'5']
                        | [b'1', b'6']
                        | [b'1', b'7']
                        | [b'1', b'8']
                        | [b'1', b'9']
                        | [b'2', b'0']
                        | [b'2', b'1']
                        | [b'2', b'2']
                        | [b'2', b'3']
                        | [b'2', b'4']
                        | [b'2', b'5']
                        | [b'2', b'6'] => 1,
                        _ => 0,
                    } * prev_prev)
                        % MOD)
                    % MOD,
            )
        }
        return prev as i32;
    }
}
