"""Plays a game where the user types random words within a time limit."""

import random
import time
import word_bank

def make_difficulty_choice():
    """Returns the user's choice of difficulty level."""
    valid_difficulty = ["easy", "medium", "hard", "extreme", "nightmare"]
    difficulty_choice = ""
    while difficulty_choice not in valid_difficulty:
        difficulty_choice = input(
        "Choose a difficulty level. \n  easy, medium, hard, "
        "extreme, \n  or nightmare: "
        ).lower()
    
    return difficulty_choice

def seconds_to_play(difficulty_level):
    """Determines how many seconds the player has for each round"""
    """Nightmare mode will have 8 seconds instead of 10"""
    seconds = 0
    if difficulty_level == "nightmare":
        seconds = 8
    else: 
        seconds = 10
    return seconds

def mode_summary(difficulty_level, round_time_limit):
    if difficulty_level == "easy":
        print("Easy mode: \n 1-3 short words \n " +str(round_time_limit) + " second limit.")
    elif difficulty_level == "medium":
        print("Medium mode \n 1-3 medium words \n " +str(round_time_limit) + " second limit")
    elif difficulty_level == "hard":
        print("Hard mode \n 1-3 long words \n " +str(round_time_limit) + " second limit")
    elif difficulty_level == "extreme":
        print("Hard mode \n 2-4 long words \n " +str(round_time_limit) + " second limit")
    elif difficulty_level == "nightmare":
        print("Nightmare mode \n 2-4 long words \n " +str(round_time_limit) + " second limit")

def play_round(words, seconds, round_num):
    """Returns True if the user successfully completed the round."""
    print("Round " + str(round_num) + ":")
          
    # Run a stopwatch for the time it takes the user to respond.
    start = time.time()
    response = input(words + "\n")
    stop = time.time()

    # Fail the round if a word is mispelled or if time runs out.
    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    if word_length == "extreme" or word_length == "nightmare":
        for word in range(num_words + 1):
            word = get_random_word(word_length)
            words = words + " " + word
    else:
        for word in range(num_words):
            word = get_random_word(word_length)
            words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "nightmare":
        words = word_bank.hard_words
    elif mode == "extreme":
        words = word_bank.hard_words
    elif mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)
