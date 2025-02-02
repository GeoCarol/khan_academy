def get_score(bananas, apples, cherries, mangoes, has_poison_apple):
    """Returns a player's total score based on their cards of each type."""
    banana_score = get_banana_score(bananas)
    apple_score = get_apple_score(apples, has_poison_apple)
    cherry_score = get_cherry_score(cherries)
    mango_score = get_mango_score(mangoes)

    total_score = banana_score + apple_score + cherry_score + mango_score
    return "\nTotal Score= " + str(total_score) + "\n" \
    + "  Apple Score= " + str(apple_score) + "\n" \
    + "  Banana Score= " + str(banana_score) + "\n" \
    + "  Cherry Score= " + str(cherry_score) + "\n" \
    + "  Mango Score= " + str(mango_score)

def get_banana_score(num_bananas):
    """Returns a player's score based on the number of banana cards."""
    # Bananas are worth more in bunches.
    if num_bananas == 1:
        return 1
    elif num_bananas == 2:
        return 4
    elif num_bananas >= 3:
        return 10
    else:
        return 0

def get_cherry_score(num_cherries):
    """Returns a player's score based on the number of cherry cards."""
    # Cerries are worth 5 points per pair.
    cherry_score = (num_cherries // 2) * 5
    return cherry_score

def get_mango_score(num_mangoes):
    """Returns a player's score based on the number of mango cards."""
    # Mangoes are worth 3 points each only if the player has an even number.
    if num_mangoes % 2 == 0:
        mango_score = num_mangoes * 3
    else:
        mango_score = 0
    return mango_score

def get_apple_score(num_apples, has_poison_apple):
    """Returns a player's score based on the number of apple cards."""
    if has_poison_apple:
        apple_score = num_apples * -2
    else:
        apple_score = num_apples * 2
    return apple_score

# Calculate the final score for each player.
player1_score = get_score(3, 2, 3, 4, True)
player2_score = get_score(1, 5, 4, 7, False)

print("Scores: Player 1" + str(player1_score) + "\n" \
      + "Scores: Player 2" + str(player2_score))
