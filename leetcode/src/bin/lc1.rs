pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
  for (index, i) in nums.clone().iter().enumerate() {
      if i > &target {
          continue;
      }
      for j in (index+1)..nums.len() {
        println!("{:?}", j);
          if (*i as usize + nums[j] as usize) as i32 == target {
              return vec![*i, nums[j]]
          }
      }
  }
  return vec![0, 0]
}

fn main() {
  let nums = vec![2,7,11,15];
  let target = 9;
  let res = two_sum(nums, target);
  println!("{:?}", res);
}