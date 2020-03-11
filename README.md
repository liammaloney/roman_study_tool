# Roman Civilization Quizzes
Very basic study tool for CLA1102 Roman Civilization

The content of these quizzes is meant to help study for the CLA1102 course at the University of Ottawa but can help anyone learn a little more about Roman dates, provinces and cities

## Dependencies
- Python 3

## Quizzes available
### Cities
The cities quiz involves a few cities that are relevant to Roman history as well as some more well known cities to give the user some geographic context.

In order to use the cities quiz, the accompanying map is required and can be found in `reference_material.pdf` There are letters marked on the map and when a city name is shown, the user is meant to enter the letter that corresponds with that city.


### Provinces
The provinces quiz tests the user's knowledge of the locations and names of all the roman provinces

In order to use the provinces quiz, the accompanying map is required and can be found in `reference_material.pdf`. There are numbers marked on the map and when a province name is shown, the user is meant to enter the number that corresponds with that city.


### Dates
The dates quiz tests the user's knowledge of some of the important dates from Roman history.

The event is given to the user and the user is asked to enter the date that that event occured.
There are 3 types of answers in this quiz
- Years: these answers will involve a single year. Eg: 146
- Ranges: these answers will involve a range of years and have the prefix `RANGE`. Eg: 123-122
- Dates: these answers will involve a specific day, month and year and have the prefix `DAY (# month year)`. The format is `15 march 44`


## Directions
Currently this program only works through the command line

1. Clone the repository

2. Within the main directory of the project, run the following command:
```
py -3 study_randomizer.py
```

3. The program will ask which quiz you would like to do. The possible answers are `cities`, `provinces`, or `dates`.

4. The program will provide you with a series of quizzes according to what is described in the Quizzes available section of this document. It will keep track of your current streak

5. If you complete all the questions in the quiz, you will see a success message, press ctrl-c to exit and see your highest streak in that session

6. If you wish to end your session before winning, press ctrl-c and then enter to exit and see your high score.
