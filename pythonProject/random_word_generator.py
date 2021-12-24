from random import randint


def pick_random_word():
    word_list = ["Hulk", "Iron Man", "Captain America", "Thor", "Black Widow", "Wanda", "Vision", "Hawkeye",
                 "Captain Marvel",
                 "Doctor Strange", "Winter Soldier", "Spider-Man", "Black Panther", "Ant-Man", "Rocket", "Star Lord",
                 "Wong",
                 "Avengers"]
    selected_index = randint(0, len(word_list) - 1)
    return word_list[selected_index]
