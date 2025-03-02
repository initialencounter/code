use std::collections::HashMap;

pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
  let floor_len = floor.len() as i32;
  if num_carpets * carpet_len == 0 {
    let mut count = 0;
    for(c, _) in floor.chars().zip(0..floor_len) {
      if c == '1' {
        count += 1;
      }
    }
    return count;
  }
  if num_carpets * carpet_len >= floor_len {
    return 0;
  }
  let mut dp: Vec<Vec<i32>> = vec![vec![0; num_carpets as usize]; floor_len as usize];
  dp[0][0] = *&floor[0..1].parse::<i32>().unwrap();
  dp[0][1] = *&floor[0..1].parse::<i32>().unwrap();
  dp[1][0] = *&floor[0..2].parse::<i32>().unwrap();
  dp[1][1] = *&floor[0..3].parse::<i32>().unwrap();
  let binary_array: Vec<u8> = floor.chars().map(|c| c.to_digit(10).unwrap() as u8).collect();
  let mut map: HashMap<&str, i32> = HashMap::new();
  let mut max_cover_white = 0;
  let mut count = 0;
  for i in 2..floor_len as usize {
    for j in 2..num_carpets as usize {
      dp[i][j] = 0;
    }
  }
  while count + carpet_len as usize <= floor_len as usize {
    let slice = &floor[count..count+carpet_len as usize];
    if let Some(&val) = map.get(slice) {
      max_cover_white += val;
    }else {
      let white_tiles = get_white_tiles(slice);
      map.insert(slice, white_tiles);
      max_cover_white += white_tiles;
    }
    println!("{:?}", slice);
    count += carpet_len as usize;
  }
  println!("{:?}", &floor[count..floor_len as usize]);
  println!("{:?}", binary_array);
  println!("{:?}", max_cover_white);
  return 0;
}

fn get_combinations_of_carpets(carpet_len: i32) -> i32 {
  let mut count = 0;
  let mut white_tiles = 0;
  let mut max_white_tiles = 0;
  let mut max_white_tiles_index = 0;
  let mut max_white_tiles_map: HashMap<i32, i32> = HashMap::new();
  while count + carpet_len as usize <= floor.len() {
    let slice = &floor[count..count+carpet_len as usize];
    white_tiles = get_white_tiles(slice);
    if white_tiles > max_white_tiles {
      max_white_tiles = white_tiles;
      max_white_tiles_index = count;
    }
    max_white_tiles_map.insert(count as i32, white_tiles);
    count += carpet_len as usize;
  }
  println!("{:?}", max_white_tiles_map);
  return 0;
}

fn get_white_tiles(slice: &str) -> i32 {
  let mut white_tiles = 0;
  for c in slice.chars() {
    if c == '1' {
      white_tiles += 1;
    }
  }
  return white_tiles;
}
fn main() {
  let binary_str = "1010001001010010001".to_string();
  let num_carpets = 2;
  let _ = minimum_white_tiles(binary_str, 0, 5);
}