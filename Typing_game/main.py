import typer

print("Type the words and hit enter within the time limit!")

# The user chooses their difficulty level
difficulty_level = typer.make_difficulty_choice()
round_time_limit = typer.seconds_to_play(difficulty_level)
level_summary = typer.mode_summary(difficulty_level, round_time_limit)

# Confirm the player is ready to play
ready = input("** Ready to play? Press any key to start! **")
                 
# Play three rounds of a speed typing game.
for round in range(1, 4):
    
    words_to_type = typer.pick_random_words(round, difficulty_level)
    passed = typer.play_round(words_to_type, round_time_limit, round)
    if not passed:
        print("\n  ** Too bad.  Better luck next time. **")
        break
    else:
        print("\n  ** You did it!!  Thanks for playing! **")
