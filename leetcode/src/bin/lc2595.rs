struct Solution;
impl Solution {
    pub fn even_odd_bit(n: i32) -> Vec<i32> {
        let mut even = 0;
        let mut odd = 0;
        let base = 2;
        let mut nn = n;
        let mut list: Vec<i32> = vec![];
        let mut r = nn % base;
        let mut index = -1;
        loop {
            r = nn % base;
            index += 1;
            if index % 2 == 0 {
                even += r;
            } else {
                odd += r;
            }
            list.insert(0, r);
            nn = (nn - r) / base;
            if nn < base {
                r = nn % base;
                index += 1;
                if index % 2 == 0 {
                    even += r;
                } else {
                    odd += r;
                }
                list.insert(0, nn);
                break;
            }
        }
        // println!("{:?}", list);
        // println!("even: {}, odd: {}", even, odd);
        return vec![even, odd];
    }
}

fn get_bytes_array(n: i32) -> Vec<i32> {
    let mut even = 0;
    let mut odd = 0;
    let base = 2;
    let mut nn = n;
    let mut list: Vec<i32> = vec![];
    let mut r = nn % base;
    let mut index = -1;
    loop {
        r = nn % base;
        index += 1;
        if index % 2 == 0 {
            even += r;
        } else {
            odd += r;
        }
        list.insert(0, r);
        nn = (nn - r) / base;
        if nn < base {
            r = nn % base;
            index += 1;
            if index % 2 == 0 {
                even += r;
            } else {
                odd += r;
            }
            list.insert(0, nn);
            break;
        }
    }
    println!("{:?}", list);
    println!("even: {}, odd: {}", even, odd);
    return vec![even, odd];
}

fn main() {
    let n = 2;
    // let res = Solution::even_odd_bit(n);
    get_bytes_array(n);
}
