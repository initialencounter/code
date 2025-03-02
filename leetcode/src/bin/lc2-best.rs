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
        let mut add1 = false;
        let mut ll1 = l1.clone();
        let mut ll2 = l2.clone();
        let mut dummy = ListNode::new(0); // 哨兵节点
        let mut cur = &mut dummy;
        let mut carry = 0;
        while ll1.is_some() || ll2.is_some() || carry != 0 {
            let mut sum = carry;
            if let Some(node1) = ll1 {
                sum += node1.val;
                ll1 = node1.next;
            }
            if let Some(node2) = ll2 {
                sum += node2.val;
                ll2 = node2.next;
            }
            carry = sum / 10;

            cur.next = Some(Box::new(ListNode::new(sum % 10)));
            cur = cur.next.as_mut().unwrap();
        }
        return dummy.next;
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

fn node_rev(node: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut node = node;
    let mut res = None;
    while let Some(box1) = node {
        res = Some(Box::new(ListNode {
            val: box1.val,
            next: res,
        }));
        node = box1.next;
    }
    return res;
}
fn main() {
    let mut l1 = write_node(vec![2, 4, 9]);
    let mut l2 = write_node(vec![5, 6, 4, 9]);
    // 7,0,4,0,1
    // let res = Solution::add_two_numbers(l1, l2);
    // println!("{:?}", res);
    // println!("{:?}", l1.unwrap().val);
    println!("{:?}", l1);
    let rev_node = node_rev(l1);
    println!("{:?}", rev_node);
}
