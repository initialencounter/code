use std::collections::HashMap;

struct RangeFreqQuery {
    map: HashMap<i32, Vec<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RangeFreqQuery {
    fn new(arr: Vec<i32>) -> Self {
        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();
        for (index, i) in arr.clone().iter().enumerate() {
            map.entry(*i).or_insert_with(Vec::new).push(index as i32)
        }
        RangeFreqQuery { map }
    }

    fn query(&self, left: i32, right: i32, value: i32) -> i32 {
        if let Some(index_list) = self.map.get(&value) {
            let res = counter(&index_list, left, right) as i32;
            return res;
        }
        return 0;
    }
}
fn binary_search(arr: &Vec<i32>, position: i32) -> i32 {
    let mut res = 0;
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;
    while left <= right {
        let mid = (right + left) / 2;
        res = left;
        if arr[mid as usize] == position {
            res = mid;
            break;
        } else if arr[mid as usize] < position {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    res
}

fn counter(arr: &Vec<i32>, value1: i32, value2: i32) -> i32 {
    let mut res1 = 0;
    let mut res2 = 0;
    if value1 <= arr[0] {
        res1 = 0;
    } else if value1 > arr[arr.len() - 1] {
        return 0;
    } else if value1 == arr[arr.len() - 1] {
        return 1;
    } else {
        res1 = binary_search(arr, value1);
        if arr[res1 as usize] < value1 {
            res1 += 1;
        }
    }
    if value2 >= arr[arr.len() - 1] {
        res2 = arr.len() as i32 - 1;
    } else if value2 < arr[0] {
        return 0;
    } else if value2 == arr[0] {
        return 1;
    } else {
        res2 = binary_search(arr, value2);
        if arr[res2 as usize] > value2 {
            res2 -= 1;
        }
    }
    return res2 - res1 + 1;
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * let obj = RangeFreqQuery::new(arr);
 * let ret_1: i32 = obj.query(left, right, value);
 */

fn main() {
    let arr = vec![1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let obj = RangeFreqQuery::new(arr);
    let ret_1: i32 = obj.query(1, 10, 1);
    println!("{:?}", ret_1);
}