[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/zVdVrHJA)
# Assignment 4: UW-Euchre

## Objectives

* Utilize data structure implementations you created before
  * If you aren't comfortable using the code you wrote for Assignment 3, send a note to Instructors on Piazza and we'll provide an alternative.
* Implement your first sort function
* Become familiar with a Python testing framework 

# Overview

Last week, you implemented some data structures that allowed you to model 
a deck of cards and work with them. This week, you're going to use that implementation 
to build out the game logic, resulting in a game you can play. 

Additionally, we'll start using the unittest testing module. This time, we've 
provided some example tests to get started, but it will likely be helpful for you 
to write some tests of your own. 

# Details 

As a reminder, the rules of UW-Euchre are below. UW-Euchre is inspired by Euchre, but 
some of the play details are simplified to make it easier to understand and implement. 


## Basic Rules Of UW-Euchre

UW-Euchre is a 2-player game. The player with the most points after 5 rounds wins. 
A player wins a round by "collecting the most tricks". 
A round consists of each player being dealt 5 cards, choosing a trump 
(a suit designated as the highest/most powerful for this round), 
and then each player takes turns playing cards for a "trick". 

A player wins a trick by playing the highest value card. 
There are a couple of rules that must be followed for playing a card: 
the first player can play any card, but the second player must "follow suit": 
if they have a card of the same suit, they must play it (but they can choose 
which card they want to play). Further, a card of the trump suit is higher 
than all other cards in the deck. For example, if Spades is trump, a 9 of Spades is 
higher than an Ace of Diamonds. Within a suit, including trump, the face value of the 
card is highest, with Aces being the highest value card.

In this version of the game, Player 1 (the computer) ALWAYS goes first and 
leads the first card. This makes the game less fun, but more simple to implement.

The deck used for UW-Euchre is a subset of the traditional 52-card deck. 
It includes the Ace, King, Queen, Jack, 10 & 9 of all four suits (Spades, Diamonds, 
Hearts, and Clubs).

## Provided Starter Code

* `a3.py` is the same starter file from A3. It's here for reference/convenience; feel free to replace it with your file. 
* `a3_test.py` provides some tests to ensure your A3 code works properly. 
* `a4.py` specifies the functions you need to implement for this assignment. 
* `a4_test.py` provides some tests to ensure your new A4 functions work properly. 
* `a4_game.py` provides code that actually runs the game. 
  * If your a3 and a4 code is correct, the game will play properly. Have fun! 

## Running 

To run tests: 

In the terminal window, run: 

```bash
python3 a4_test.py
```
or for A3 tests: 

```bash
python3 a3_test.py
```

To run the game: 

```shell
python3 a4_game.py
```

# Notes

* Any updates or clarifications to the assignment will be noted here and on Piazza. 
* 
