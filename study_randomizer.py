from data import *
import random

def game(quizzable_data):
    high_score = 0
    try :
        streak = 0
        done = []
        num_entries = len(quizzable_data)
        while (True):
            randnum = random.randrange(0,num_entries)
            question = list(quizzable_data.keys())[randnum]

            while question in done:
                randnum = random.randrange(0,num_entries)
                question = list(quizzable_data.keys())[randnum]

            print(question)

            answer = input("Input Answer: ").upper()

            if (answer == quizzable_data[question].upper()):
                streak = streak + 1
                done.append(question)
                if (streak > high_score):
                    high_score = streak
                print("Correct.\n\n")
            else:
                streak = 0
                print("Incorrect, Correct answer is {}\n\n".format(quizzable_data[question]))
            print("Current Streak: {}\n".format(streak))

            if (len(done)>=num_entries):
                print('YOU WIN')
                exit
    except KeyboardInterrupt:
        print('Exited, your high score was {}'.format(high_score))

if __name__ == "__main__":
    data_type = input("What would you like to be quizzed on? Cities, Dates, or Provinces?: ")
    if(data_type.lower() == 'provinces'):
        game(PROVINCES)
    elif(data_type.lower() == 'dates'):
        game(DATES)
    elif(data_type.lower() == 'cities'):
        game(CITIES)