use std::collections::HashMap;
struct FoodRatings {
    foods: Vec<String>,
    ratings: Vec<i32>,
    cusi_map: HashMap<String, Vec<usize>>,
    food_index_map: HashMap<String, usize>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FoodRatings {
    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut map: HashMap<String, Vec<usize>> = HashMap::new();
        let mut food_index_map: HashMap<String, usize> = HashMap::new();
        for i in 0..foods.len() {
            food_index_map.insert(foods[i].clone(), i);
            map.entry(cuisines[i].clone()).or_insert(vec![]).push(i);
        }
        FoodRatings {
            foods,
            ratings,
            cusi_map: map,
            food_index_map,
        }
    }

    fn change_rating(&mut self, food: String, new_rating: i32) {
        let index = self.food_index_map.get(&food).unwrap();
        self.ratings[*index] = new_rating;
    }

    fn highest_rated(&self, cuisine: String) -> String {
        let mut highest_rating = 0;
        let mut highest_rated_food = String::new();
        let foods_list = self.cusi_map.get(&cuisine).unwrap();
        for i in foods_list {
            if self.ratings[*i] > highest_rating {
                highest_rating = self.ratings[*i];
                highest_rated_food = self.foods[*i].clone();
            }
            if self.ratings[*i] == highest_rating {
              if self.foods[*i].clone() < highest_rated_food {
                highest_rated_food = self.foods[*i].clone();
              }
          }
        }
        return highest_rated_food;
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings::new(foods, cuisines, ratings);
 * obj.change_rating(food, newRating);
 * let ret_2: String = obj.highest_rated(cuisine);
 */

fn main() {
    // let mut obj = FoodRatings::new(
    //     vec![
    //         "kimchi".to_string(),
    //         "miso".to_string(),
    //         "sushi".to_string(),
    //         "moussaka".to_string(),
    //         "ramen".to_string(),
    //         "bulgogi".to_string(),
    //     ],
    //     vec![
    //         "korean".to_string(),
    //         "japanese".to_string(),
    //         "japanese".to_string(),
    //         "greek".to_string(),
    //         "japanese".to_string(),
    //         "korean".to_string(),
    //     ],
    //     vec![9, 12, 8, 15, 14, 7],
    // );
    // println!("{:?}", obj.highest_rated("korean".to_string()));
    // println!("{:?}", obj.highest_rated("japanese".to_string()));
    // obj.change_rating("sushi".to_string(), 16);
    // println!("{:?}", obj.highest_rated("japanese".to_string()));
    // obj.change_rating("ramen".to_string(), 16);
    // println!("{:?}", obj.highest_rated("japanese".to_string()));
    // [[["cpctxzh","bryvgjqmj","wedqhqrmyc","ee","lafzximxh","lojzxfel","flhs"],
    // ["wbhdgqphq","wbhdgqphq","mxxajogm","wbhdgqphq","wbhdgqphq","mxxajogm","mxxajogm"],
    // [15,5,7,16,16,10,13]],
    // ["lojzxfel",1],["mxxajogm"],["wbhdgqphq"],["mxxajogm"]]
    let mut obj = FoodRatings::new(
        vec![
            "cpctxzh".to_string(),
            "bryvgjqmj".to_string(),
            "wedqhqrmyc".to_string(),
            "ee".to_string(),
            "lafzximxh".to_string(),
            "lojzxfel".to_string(),
            "flhs".to_string(),
        ],
        vec![
            "wbhdgqphq".to_string(),
            "wbhdgqphq".to_string(),
            "mxxajogm".to_string(),
            "wbhdgqphq".to_string(),
            "wbhdgqphq".to_string(),
            "mxxajogm".to_string(),
            "mxxajogm".to_string(),
        ],
        vec![15, 5, 7, 16, 16, 10, 13],
    );
    println!("{:?}", obj.change_rating("lojzxfel".to_string(), 1));
    println!("{:?}", obj.highest_rated("mxxajogm".to_string()));
    println!("{:?}", obj.highest_rated("wbhdgqphq".to_string()));
    println!("{:?}", obj.highest_rated("mxxajogm".to_string()));
}
