= Galaxy Defender
:toc:
:icons: font
:source-highlighter: highlight.js

A lightweight arcade-style space shooter created with Python and Pygame. Dodge incoming enemies, shoot them down, and try to achieve the highest score possible.

== Overview

Galaxy Defender is a beginner-friendly project that demonstrates the fundamentals of game development with Pygame, including:

* Real-time keyboard input
* Collision detection
* Object spawning
* Score tracking
* Basic game loop architecture

== Installation

=== Clone the Repository

## [source,bash]

git clone https://github.com/yourusername/galaxy-defender.git
cd galaxy-defender
------------------

=== Install Dependencies

## [source,bash]

## pip install pygame

== Start the Game

## [source,bash]

## python game.py

== Controls

[cols="1,2",options="header"]
|===
|Input |Function

|← / →
|Move spaceship

|Space
|Fire projectile

|Esc
|Quit the game

|===

== Game Rules

* Destroy enemy ships to earn points.
* Avoid collisions with enemies.
* The game ends immediately after a collision.
* Try to survive as long as possible.

== Project Layout

## [source,text]

.
├── game.py
├── assets/
│   ├── player.png
│   ├── enemy.png
│   └── laser.wav
├── README.adoc
└── LICENSE
-----------

== Possible Enhancements

* Boss battles
* Animated explosions
* Soundtrack and sound effects
* Multiple weapon types
* Health system
* Difficulty scaling
* Local high-score storage

== Technologies Used

* Python
* Pygame

== Contributing

Contributions are welcome. Feel free to fork the project, create a feature branch, and submit a pull request with improvements or bug fixes.

== License

Licensed under the MIT License.
