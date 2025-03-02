use std::collections::HashMap;

struct Allocator {
    n: i32,
    pub memory: Vec<i32>,
    map: HashMap<i32, Vec<i32>>, // m_id, index
    free_list: Vec<[i32; 2]>,    // vec[index, len]
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */

impl Allocator {
    fn new(n: i32) -> Self {
        let map: HashMap<i32, Vec<i32>> = HashMap::new();
        let free_list: Vec<[i32; 2]> = vec![[0, n]];
        Allocator {
            n,
            memory: vec![0; n as usize],
            map,
            free_list,
        }
    }
    // 1. 从做左侧找到空闲块
    // 记录空闲块长度，下标【len, [index]】// 更新
    // 2. 分配内存
    fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        self.free_list.sort_by_key(|item| item[0]);
        let mut count = 0;
        for [index, free_len] in self.free_list.clone() {
            if free_len >= size {
                for i in index..index + size {
                    self.memory[i as usize] = m_id;
                    self.map.entry(m_id).or_insert(vec![]).push(i);
                }
                if free_len > size {
                    self.free_list.remove(count as usize);
                    self.free_list.push([index + size, free_len - size]);
                } else if free_len == size {
                    self.free_list.remove(count as usize);
                }
                return index;
            }
            count += 1;
        }
        return -1;
    }

    // Allocator loc = new Allocator(10); // 初始化一个大小为 10 的内存数组，所有内存单元都是空闲的。
    // loc.allocate(1, 1); // 最左侧的块的第一个下标是 0 。内存数组变为 [1, , , , , , , , , ]。返回 0 。【9】
    // loc.allocate(1, 2); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,2, , , , , , , , ]。返回 1 。【8】
    // loc.allocate(1, 3); // 最左侧的块的第一个下标是 2 。内存数组变为 [1,2,3, , , , , , , ]。返回 2 。【7】
    // loc.freeMemory(2); // 释放 mID 为 2 的所有内存单元。内存数组变为 [1, ,3, , , , , , , ] 。返回 1 ，因为只有 1 个 mID 为 2 的内存单元。【1，7】
    // loc.allocate(3, 4); // 最左侧的块的第一个下标是 3 。内存数组变为 [1, ,3,4,4,4, , , , ]。返回 3 。【1， 4】
    // loc.allocate(1, 1); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,1,3,4,4,4, , , , ]。返回 1 。【4】
    // loc.allocate(1, 1); // 最左侧的块的第一个下标是 6 。内存数组变为 [1,1,3,4,4,4,1, , , ]。返回 6 。【3】
    // loc.freeMemory(1); // 释放 mID 为 1 的所有内存单元。内存数组变为 [ , ,3,4,4,4, , , , ] 。返回 3 ，因为有 3 个 mID 为 1 的内存单元。【2，4】
    // loc.allocate(10, 2); // 无法找出长度为 10 个连续空闲内存单元的空闲块，所有返回 -1
    fn free_memory(&mut self, m_id: i32) -> i32 {
        if let Some(indexs) = self.map.clone().get(&m_id) {
            for index in indexs {
                self.memory[*index as usize] = 0;
                self.free_list.push([*index, 1]);
            }
            self.merge_free_list();
            self.map.remove(&m_id);
            return indexs.len() as i32;
        }
        return 0;
    }
    fn merge_free_list(&mut self) {
        self.free_list.sort_by_key(|item| item[0]);
        for i in 0..self.free_list.len() {
            if i + 1 >= self.free_list.len() {
                break;
            }
            if self.free_list[i][0] + self.free_list[i][1] == self.free_list[i + 1][0] {
                self.free_list[i][1] += self.free_list[i + 1][1];
                self.free_list.remove(i + 1);
                if i + 1 >= self.free_list.len() {
                    break;
                }
                if self.free_list[i][0] + self.free_list[i][1] == self.free_list[i + 1][0] {
                    self.merge_free_list();
                }
            }
        }
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * let obj = Allocator::new(n);
 * let ret_1: i32 = obj.allocate(size, mID);
 * let ret_2: i32 = obj.free_memory(mID);
 */

fn main() {
    // let n = 7;
    // let mut obj = Allocator::new(n);
    // println!("{}", obj.allocate(7, 8));
    // println!("{}", obj.allocate(8, 7));
    // println!("{}", obj.allocate(6, 2));
    // println!("{}", obj.free_memory(9));
    // println!("{:?}", obj.memory);
    // println!("{}", obj.free_memory(8));
    // println!("{:?}", obj.memory);
    // println!("{}", obj.allocate(7, 6));
    // println!("{}", obj.free_memory(9));
    // println!("{}", obj.allocate(10, 9));

    // [[10],[1,1],[1,2],[1,3],[2],[3,4],[1,1],[1,1],[1],[10,2],[7]]
    // let n = 10;
    // let mut obj = Allocator::new(n);
    // println!("{}", obj.allocate(1, 1));
    // println!("{}", obj.allocate(1, 2));
    // println!("{}", obj.allocate(1, 3));
    // println!("{}", obj.free_memory(2));
    // println!("{}", obj.allocate(3, 4));
    // println!("{}", obj.allocate(1, 1));
    // println!("{}", obj.allocate(1, 1));
    // println!("{}", obj.free_memory(1));
    // println!("{:?}", obj.memory);
    // println!("{}", obj.allocate(10, 2));
    // println!("{}", obj.free_memory(7));
    let list: Vec<Vec<i32>> = vec![vec![161],vec![62],vec![19,105],vec![24],vec![12,128],vec![105],vec![24],vec![47,161],vec![24],vec![166,110],vec![110],vec![47],vec![107,31],vec![137,79],vec![22],vec![22],vec![28,185],vec![59,106],vec![185],vec![110],vec![177,108],vec![112,119],vec![185,109],vec![6,159],vec![15],vec![198,100],vec![100],vec![47],vec![5,93],vec![188,153],vec![159],vec![134],vec![93],vec![153],vec![185],vec![129,58],vec![25,15],vec![23,159],vec![50,196],vec![110,101],vec![128],vec![4],vec![110,122],vec![159],vec![135,40],vec![110],vec![22]];
    let n = 168;
    let mut obj = Allocator::new(n);
    for i in 0..list.len() {
        println!("i:{:?}",list[i]);
        println!("i:{:?}",obj.memory);
        println!("i:{:?}",obj.free_list);
        if list[i].len() == 1 {
            println!("{}", obj.free_memory(list[i][0]));
        } else {
            println!("{}", obj.allocate(list[i][0], list[i][1]));
        }
        println!("\n");
    }
}
