from roman_provinces import *
import random

if __name__ == "__main__":
    high_score = 0
    try :
        streak = 0
        done = []
        while (True):
            randnum = random.randrange(0,49)
            province_name = list(PROVINCES.keys())[randnum]

            while province_name in done:
                randnum = random.randrange(0,49)
                province_name = list(PROVINCES.keys())[randnum]

            print(province_name)

            answer = input("Input Answer: ")

            if (answer == PROVINCES[province_name]):
                streak = streak + 1
                done.append(province_name)
                if (streak > high_score):
                    high_score = streak
                print("Correct.\n")
            else:
                streak = 0
                print("Incorrect, Correct answer is {}\n".format(PROVINCES[province_name]))
            print("Current Streak: {}".format(streak))

            if (len(done)>=len(PROVINCES)):
                print('YOU WIN')
                exit
    except KeyboardInterrupt:
        print('Exited, your high score was {}'.format(high_score))
