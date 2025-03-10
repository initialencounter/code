// 2269. 找到一个数字的 K 美丽值
// 简单
// 相关标签
// 相关企业
// 提示
// 一个整数 num 的 k 美丽值定义为 num 中符合以下条件的 子字符串 数目：

// 子字符串长度为 k 。
// 子字符串能整除 num 。
// 给你整数 num 和 k ，请你返回 num 的 k 美丽值。

// 注意：

// 允许有 前缀 0 。
// 0 不能整除任何值。
// 一个 子字符串 是一个字符串里的连续一段字符序列。

 

// 示例 1：

// 输入：num = 240, k = 2
// 输出：2
// 解释：以下是 num 里长度为 k 的子字符串：
// - "240" 中的 "24" ：24 能整除 240 。
// - "240" 中的 "40" ：40 能整除 240 。
// 所以，k 美丽值为 2 。
// 示例 2：

// 输入：num = 430043, k = 2
// 输出：2
// 解释：以下是 num 里长度为 k 的子字符串：
// - "430043" 中的 "43" ：43 能整除 430043 。
// - "430043" 中的 "30" ：30 不能整除 430043 。
// - "430043" 中的 "00" ：0 不能整除 430043 。
// - "430043" 中的 "04" ：4 不能整除 430043 。
// - "430043" 中的 "43" ：43 能整除 430043 。
// 所以，k 美丽值为 2 。

struct Solution;
use std::collections::HashMap;


impl Solution {
  pub fn divisor_substrings(num: i32, k: i32) -> i32 {
      let mut map: HashMap<&str, bool> = HashMap::new(); 
      let source_string = num.to_string();
      let source_string_len = source_string.len() as i32;
      let last = source_string_len - k;
      let mut res = 0;
      for i in 0..=last {
          let sub_string = &source_string[(i) as usize..(i+k) as usize];
          if let Some(_) = map.get(sub_string) {
              res += 1;
          }else {
              let sub_string_num = sub_string.parse::<i32>().unwrap();
              if sub_string_num != 0 && num % sub_string_num == 0 {
                  res += 1;
                  map.insert(sub_string, true);
              }
          }
      }
      return res;
  }
}

fn main(){
  println!("{}", Solution::divisor_substrings(240, 2))
}