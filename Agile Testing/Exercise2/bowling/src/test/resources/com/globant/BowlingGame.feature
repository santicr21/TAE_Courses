Feature: Bowling Game Score

As a bowler
I want to calculate my bowling game score
So that I can know the winner

Scenario: Gutter game
  Given a bowling game
  When I roll the following line "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
  Then my score is 0

Scenario: Game all ones
  Given a bowling game
  When I roll the following line "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"
  Then my score is 20

