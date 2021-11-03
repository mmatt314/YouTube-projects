import random
import matplotlib.pyplot as plt


def play_game():
    survivors = 16
    tiles_remaining = 18

    attempt_after_forgetting = "first"
    attempts_at_using_light = "first"

    while True:
        choice = random.choice(["tempered", "normal"])
        #  comment out some or all of the next 3 blocks of code to explore the impact of each player's actions

        if survivors == 13 and attempt_after_forgetting == "first" and tiles_remaining < 15:
            attempt_after_forgetting = "second"
            tiles_remaining += 1

        if survivors == 8:
            if tiles_remaining > 1:
                survivors -= 3
                tiles_remaining -= 1
            elif tiles_remaining == 1:
                return 11

        if survivors == 4 and tiles_remaining > 3 and attempts_at_using_light == "first":
            attempts_at_using_light = "second"
            tiles_remaining -= 3
        elif survivors == 4 and attempts_at_using_light == "first":
            return 12

        # leave this, it's the actual gameplay
        if choice == "normal":
            survivors -= 1
            tiles_remaining -= 1  # here is where a contestant dies.

        elif choice == "tempered":
            tiles_remaining -= 1  # this is where a contestant guesses correctly

        if survivors == 0:
            return 16 - survivors  # this checks if the game should end and returns the no. of deaths

        elif tiles_remaining == 0:
            return 16 - survivors  # this checks if the game should end and returns the no. of deaths


# let's examine some of the data we generate...

number_of_runs = 10000  # how many games
total = 0
total_13 = 0
no_of_deaths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, number_of_runs + 1):
    x = play_game()
    total += x  # summing up all the survivors
    if x == 13:  # how many games will have just our 3 heroes surviving?
        total_13 += 1
    no_of_deaths[x] += 1

prob_of_death = [deaths / number_of_runs for deaths in no_of_deaths]

x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y_axis = prob_of_death

plt.bar(x_axis, y_axis)
plt.xlabel("Number of Deaths")
plt.ylabel("Probability")
plt.xticks(x_axis, x_axis)
plt.ylim([0, 0.45])
plt.title(f"Mean number of deaths = {total / number_of_runs}\n"
          f"Probability of exactly 3 survivors = {total_13 / number_of_runs}")
plt.show()
