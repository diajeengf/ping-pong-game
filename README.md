# ping-pong-game

## Project Goal
The primary objective of this project is to develop a simple Ping-Pong game prototype that includes automatic ball movement, two rackets controlled by the keyboard, and a losing condition when a player misses the ball.

---

## Classes
- ***GameSprite***: A basic class to load images, set size and position, and draw the object.
- ***Player***: Inherits from GameSprite, and adds movement with keyboard keys (W/S for left racket, UP/DOWN for right racket).

---

## Main Game Objects
- *racket1* and *racket2*: _The two rackets for each player._
- *ball*: The ball that moves and decides who loses the game.

---

## Game Logic
- The ball moves by itself.
- It bounces when it hits the paddles or the top/bottom walls.
- If the ball goes past the left edge, Player 1 loses.  
  If it goes past the right edge, Player 2 loses.

---

## Special Features of the Project
- Two-player control using keyboard keys.  
- Easy win/lose condition.

---

## Project Prospects
This game has potential for further development, including:
1. Adding a scoring system to track each player’s points.
2. Increasing the difficulty over time by speeding up the ball.
3. Implementing sound effects and background music.
