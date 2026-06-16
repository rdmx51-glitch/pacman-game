A classic arcade game "Pac-Man" implemented in Python using the Raylib library.  

---

## Features

- **Move** – arrow keys (↑w ↓s ←a →d)  
- **Ghosts** – three types with different chase strategies  
- **Scared mode** – ghosts turn blue after eating a big dot  
- **Audio** – sound effects and background music  
- **High scores** – saved locally in `scores.txt`

---

## Tech Stack

- **Language:** Python 3.12+  
- **Library:** Raylib (via `pyray` wrapper)  
- **Graphics:** Custom PNG sprites  
- **Audio:** MP3 files

---

## Build & Run

```bash
# Clone the repository
git clone https://github.com/rdmx51-glitch/pacman-game.git
cd pacman-game/pacman-mechanics

# Install dependencies
pip install -r requirements.txt

# Run the game
python pacmans.py