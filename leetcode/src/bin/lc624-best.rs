struct Solution {}
impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        let mut max_val = *arrays[0].iter().last().unwrap();
        let mut min_val = arrays[0][0];
        let mut res = 0;
        for arr in &arrays[1..arrays.len()] {
            let n = arr.len();
            res = res.max((arr[0] - max_val).abs());
            res = res.max((arr[n - 1] - min_val).abs());
            max_val = max_val.max(arr[n - 1]);
            min_val = min_val.min(arr[0]);
        }
        return res;
    }
}

fn main() {
    // [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
    let arrays = vec![vec![1, 5], vec![3, 4]];
    let result = Solution::max_distance(arrays);
    println!("{}", result);
}
