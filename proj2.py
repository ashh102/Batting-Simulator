"""
AUTHOR: Tahj Gayfield, Ashley Maynez
DATE: 08-26-2019
CLASS: CMP SCI 4500
SECTION: 001

PROGRAM DESCRIPTION:
This file will read in the three numbers from the text 'InClass2infile.txt', simulate a batter with the batting average
BatAverage batting AtBats times. For each at bat, it throws a random number between 0.0 and 1.0 from a uniform random distribution.
It uses Rseed to seed Python's random number generator. If the number that's thrown is less than or equal to the BatAverage,
then the batter gets a hit. If the number that's thrown is greater than BatAverage, the batter does not get a hit.
It does this AtBats times. When it has simulated AtBats hitting opportunities, it writes to the following text file:
'InClass2outfile.txt'.

Input File: InClass2infile.txt
Output File: InClass2outfile.txt
"""

import random

# Variable to store reference to output file.
outputFile = open("InClass2outfile.txt", "w")

# Clears the file by writing a blank character to that file.
outputFile.write("")

# Closes previous output file after clearing.
outputFile.close()

# Opens and creates object for input file.
inputFile = open("InClass2infile.txt", "r")

# Reads the # of atBats from the file and casts it to an integer.
atBats = int(inputFile.readline())

# Reads the seed value, for the random generator, from the file and casts it to an integer.
rSeed = int(inputFile.readline())

# Reads the batting average from the file and casts it to an integer.
batAverage = float(inputFile.readline())

# Supplies the random number generator with the seed value from the input file.
random.seed(rSeed)

# Declares "constants" for the integer values of a hit or miss.
HIT = 1
MISS = 0

# Declares integers to keep track of the amount of hits and misses.
totalHits = 0
totalMisses = 0

# Declares list to store outcomes of each atBat (hit or miss).
outcomes = []

# Declares variable to count longest trend of hits in a row.
hitsInRow = 0

# Stores the longest streak of hits in a row.
maxStreakOfHitsInRow = 0

# Iterates atBat number of times and records hits and misses.
for i in range(0, atBats - 1):
    randNum = random.uniform(0.0, 1.0)

    # Hits.
    if randNum <= batAverage:
        totalHits += 1
        outcomes.append(HIT)
        hitsInRow += 1
        if hitsInRow > maxStreakOfHitsInRow:
            maxStreakOfHitsInRow = hitsInRow

    # Misses.
    elif randNum > batAverage:
        totalMisses += 1
        outcomes.append(MISS)
        hitsInRow = 0

# Creates variable to write to output file.
outputFile = open("InClass2outfile.txt", "a")

# Outputs data to file in readable format.
outputFile.write("Seed for Python's Random Number Generator: %d\n" % rSeed)
outputFile.write("Original Batting Average: %.3f\n" % batAverage)
outputFile.write("Number of At Bats Simulated: %d\n" % atBats)
outputFile.write("\n")
outputFile.write("Number of hits: %d\n" % totalHits)
outputFile.write("Simulated Batting Average: %.3f\n" % (float(totalHits) / float(len(outcomes))))
outputFile.write("Longest Streak of Hits in a Row: %d\n" % maxStreakOfHitsInRow)

# Closes output and input file.
outputFile.close()
inputFile.close()

# Prompts user to press ENTER to complete the program
pressEnter = input("Press ENTER to finish.")
