Space Shooter Game:

A simple 2D space shooter game built with Python where you defend against incoming alien ships. I've successfully created a standalone executable so you can run the game without needing Python installed.

Game Description:

Control a spaceship at the bottom of the screen and shoot down enemy ships that move horizontally and gradually descend. The game ends when any enemy reaches near your spaceship. Try to get the highest score possible!

How to Run:

Simply double-click space_game_v1.exe - no installation needed! The game should run immediately on Windows systems.

Controls:

LEFT/RIGHT Arrow Keys - Move your spaceship

SPACEBAR - Shoot laser bullets

N Key - Restart the game when game over

X Key - Exit the game

File Details:

The executable includes all necessary files bundled together:

spaceship.png (24 KB) - Player spaceship image

enemy.png (40 KB) - Enemy ship image

bullet.png (8 KB) - Laser bullet image

bg.png (120 KB) - Background image

SPACE.ttf (111 KB) - Custom font file

laser.wav (34 KB) - Shooting sound effect

explosion.wav (329 KB) - Enemy explosion sound

background.wav (4,735 KB) - Background music

space_game_v1.exe (17,782 KB) - The game executable

Game Features:

Background music with adjustable volume

Sound effects for shooting and explosions

Dynamic enemy movement patterns

Score display with custom font

Game over screen with restart option

No dependencies or installation required

Technical Details:

Built with Python 3.x and PyGame

Compiled using PyInstaller for standalone execution

Screen resolution: 800x600 pixels

Complete game loop with collision detection

All assets bundled into single executable

If You Have Issues:

Make sure you're on Windows (the .exe is Windows-only)

Try running as administrator if the game doesn't launch

Some antivirus software might flag it initially - you can add an exception if needed

If sounds don't play, check your system volume

Building from Source (Optional)
If you want to modify the game:


bash
pip install pygame
python space_shooter.py
To create your own executable:

bash
pip install pyinstaller
pyinstaller --onefile --noconsole --add-data "*.png;." --add-data "*.wav;." --add-data "*.ttf;." space_shooter.py
Notes
This is a beginner PyGame project I created while learning game development. The executable version makes it easy to share with friends who don't have Python installed.

Author:

Created by Yassine GR as a PyGame learning project.

Game assets from various free sources

