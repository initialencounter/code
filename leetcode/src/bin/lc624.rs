struct Solution {}
use std::collections::HashMap;

impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        let mut max: i32 = 0;
        let mut map: HashMap<i32, i32> = HashMap::new();
        for (index, array) in arrays.iter().enumerate() {
            for i in array {
                let max_of_i: i32;
                if let Some(max_of_index) = map.get(i) {
                    max_of_i = *max_of_index;
                } else {
                    let mut max_of_index = 0;
                    for (index2, array2) in arrays.iter().enumerate() {
                        if index == index2 {
                            // 跳过自身所在数组
                            continue;
                        }
                        let low = &array2[0];
                        let high = array2.iter().last().unwrap();
                        let abs1: i32;
                        if i <= low {
                            abs1 = (i - high).abs();
                        } else if i >= high {
                            abs1 = (i - low).abs();
                        } else {
                            let abs2 = (i - low).abs();
                            let abs3 = (i - high).abs();
                            abs1 = abs2.max(abs3);
                        }
                        if abs1 > max_of_index {
                            max_of_index = abs1;
                        }
                    }
                    max_of_i = max_of_index;
                    map.insert(*i, max_of_index);
                }
                if max_of_i > max {
                    max = max_of_i;
                }
            }
        }
        return max;
    }
}

fn main() {
    // [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
    let arrays = vec![vec![1], vec![2]];
    let result = Solution::max_distance(arrays);
    println!("{}", result);
}
