CSC226 Final Project

## Instructions

**Author(s)**: Janee Amig

**Google Doc Link**: https://docs.google.com/document/d/1LlmOOMc5_5ZcKUendxeOnrjQex5l9WWuomnUwxlZPDw/edit?tab=t.0#heading=h.qg98s23ap4mh 

---

## Milestone 1: Setup, Planning, Design

**Title**: `Cookie Conundrum`

**Purpose**: ` A working Visual Novel/Choose your own adventure, where you play as Scott and you're trying to
                 find his missing cookies.`

**Source Assignment(s)**: `T01, T04, T11, T12, HW05`

**Branches**:

```
    Branch 1 name: amigj
```
---

## Milestone 2: Code Setup and Issue Queue

```
    ** Getting started on the coding for the end and start screens. I don't have the assets yet, but soon then I'll upload.
    I'm just concerned about the coding the dialouge and buttons for choices, but I feel hopeful about it.
```

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `30%

**Confidence**:

```
   I believe I can get this done by the time of next week. Right now I am behind, and trying to work on the start
   screen before I start on the actual game code. The game code will be alot because it's going to require story options,
   buttons, and such.
   
   The plan is this:
   1) start screen [semi-hard]
   2) game code [hard]
        2a) dialouge class working
        2b) character placeholder (box)
        2c) getting the story written/so dialouge can be implemented
        2d) button options
   3) end screen [semi-hard]
        3a) get the main end screen working
        3b) optional:win screen
        3c) optional:lose screen
   4) character assets impleted to make the program look pretty [easy]
   
```
---

## Milestone 4: Final Code, Presentation, Demo

## User Instructions
The user must start the game via the start_screen.py. After hitting run, the User is given the objective of the game
and how to play.

## Reflection (what did you learn?)
To be honest this project's original idea was to ambisous and complicated for my beginner coder brain.
Plus I did wait until the last minute, but at least it wasn't the last last minute. 

I wanted to do a Visual novel due to my current instrest in looking at the Renpy engine for visual
novels. I thought it would be a fun process to draw the assets I needed. I had to learn to cut corners
with the assets by making them simple in style, plus already fitting to the window size when I imported the
images into my code. (It would of been a pain to translate the x and y of the images if I didn't.)
The original concept is there but it had to be simpfied due to the remaining time I had. Originally I was
going to have an end screen class, but deleted it due to time.

I had to watch plenty of videos, read forums, ChatGPT, and look at class resources for help.
The introdution to pygame video saved me because I didn't know what I was doing trying to make a literal
box. I enjoyed learning how to get surfaces to work and to layer them was helpful in the end. There
were times where I had to change my apporach to some ideas: Having the user mouse click a button for a choice,
but that would be too much code plus reworking code, so a key press instead is one time.

The hardest was the start screen. Then the 2 or 3 hour slump starting the game code and being clueless
on how to fix the game loop. I overlooked a lot of things and had to skim. If not skim, then have
chatGPT help me figure out what I missed. I did the majority of the game code and class making
in one day which is good.

I'm glad that I messed around on a different py project to work things out, because that helped me
alot to get the coding process down quicker. 

I know for sure this game code isn't the best. One problem is the key press counters dictating the choices.
If either 0 or 1 get pressed more than 3 times, then the game goes back to the default game screen. It's a 
bug, but it's too late to fix now. If I were to go back, I would fix the counter system or rework it to make
it better.

Plus colors were chosen to be colorblind friendly: https://davidmathlogic.com/colorblind/#%23000000-%23E69F00-%2356B4E9-%23009E73-%23F0E442-%230072B2-%23D55E00-%23CC79A7