# Advent of Code 2024 Solutions
=====================================

This repository contains my solutions to the Advent of Code 2024 challenges.

## Table of Contents
-----------------

* [Day 1: Historian Hysteria](#day-1)
* [Day 2: [Day 2 Title]](#day-2)
* ...
* [Day 25: [Day 25 Title]](#day-25)

## Solutions

### Day 1: Historian Hysteria
#### Problem Statement
You are given a list with two columns that contain numbers. Sort both columns in ascending order and compare the two values in each row. Subtract the smaller value from the larger value. The answer is the summation of these values

#### Solution
I started off my solution by reading the text file with the given input, removing the new line characters, and separating the lines by the spaces in between the values. Once the line is cleaned the values are added to their respective columns after being converted into an integer. The columns are then sorted and iterated over to calculate the difference between the maximum and minimum values. The difference is then added to the total to find the answer.

#### [See solution here](https://github.com/narrativityy/AdventOfCode24/blob/main/Day1.py)