// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
struct Solution {}
impl Solution {
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut list1 = read_node(l1);
        let mut list2 = read_node(l2.clone());
        let n = list1.len().max(list2.len());
        list1 = align(list1, n);
        list2 = align(list2, n);
        let mut res_list: Vec<i32> = vec![];
        let mut add1 = false;
        println!("{:?},\n {:?}", list1, list2);
        for i in 0..n {
            let mut sum = list1.get(i).unwrap_or(&0) + list2.get(i).unwrap_or(&0);
            if add1 {
                sum += 1;
            }
            if sum >= 10 {
                add1 = true;
                println!("sum>10: {}", sum);
                res_list.push(sum % 10);
            } else {
                add1 = false;
                println!("sum<10: {}", sum);
                res_list.push(sum);
            }
        }
        if add1 {
            res_list.push(1);
        }
        return write_node(res_list);
    }
}

fn read_node(node: Option<Box<ListNode>>) -> Vec<i32> {
    let mut res: Vec<i32> = vec![];
    if let Some(box1) = node {
        res.push(box1.val);
        res.extend(read_node(box1.next));
    }
    return res;
}

fn write_node(node: Vec<i32>) -> Option<Box<ListNode>> {
    let mut res: Option<Box<ListNode>> = None;
    for i in (0..node.len()).rev() {
        let mut new_node = ListNode::new(node[i]);
        new_node.next = res;
        res = Some(Box::new(new_node));
    }
    return res;
}

fn align(node: Vec<i32>, length: usize) -> Vec<i32> {
    let mut res = node;
    while res.len() < length {
        res.push(0);
    }
    return res;
}
fn main() {
    // let l1 = write_node(vec![2, 4, 9]);
    // let l2 = write_node(vec![5, 6, 4, 9]);
    // let res = Solution::add_two_numbers(l1, l2);
    // let res_list = read_node(res);
    // println!("{:?}", res_list);
    let mut l1 = ListNode::new(1);
    l1.next = Some(Box::new(ListNode::new(2)));
}
