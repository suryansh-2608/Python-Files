import random_word_generator
import colord


def change_current_word_state(selected_word, current_word_state, character):
    modified_word_state = ""

    for i in range(len(selected_word)):
        if current_word_state[i] == "_" and selected_word[i] == character:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]

    return modified_word_state


def input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining):
    if input_char in selected_word:
        current_word_state = change_current_word_state(selected_word, current_word_state, input_char)
    else:
        attempts_remaining -= 1
    return current_word_state, attempts_remaining


def print_current_state(current_word_state, attempts_remaining):
    colord.print_information("Current State: ", end=" ")
    for i in current_word_state:
        colord.print_information(i, end=" ")

    colord.print_warning("\tAttempts Remaining : %d" % attempts_remaining)


def check_game_status(selected_word, current_word_state, attempts_remaining):
    if current_word_state == selected_word:
        # Print in Green
        colord.print_sucess("You WON! :D")
        return True
    elif attempts_remaining <= 0:
        # Print in Red
        colord.print_failure("You Lost :(")
        # Print in Blue - for Information
        colord.print_information("Word was %s" % selected_word)
        return True
    return False


def play_game(attempts=5):
    selected_word = random_word_generator.pick_random_word()

    current_word_state = ""

    for i in range(len(selected_word)):
        if selected_word[i] == 'a' or selected_word[i] == 'e' or selected_word[i] == 'i' or selected_word[i] == 'o' or \
                selected_word[i] == 'u':
            current_word_state += selected_word[i]
        else:
            current_word_state += '_'

    attempts_remaining = attempts

    print_current_state(current_word_state, attempts_remaining)

    while True:
        input_char = input("Guess a character: ")
        print()

        current_word_state, attempts_remaining = input_character_in_word(selected_word, input_char, current_word_state,
                                                                         attempts_remaining)

        print_current_state(current_word_state, attempts_remaining)

        game_ended = check_game_status(selected_word, current_word_state, attempts_remaining)
        if game_ended:
            break


if __name__ == "__main__":
    play_game()
