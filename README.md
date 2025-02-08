# Conway's Game of Life (Pygame Simulation)

## Overview
This project is an implementation of **Conway's Game of Life** using **Pygame**. It consists of two scripts:
- `main.py`: The primary script for running the simulation.
- `claude.py`: A secondary script that incorporates AI-generated code for alternative implementations or additional features.

The simulation follows the classic rules of Conway's Life, where cells evolve based on simple survival and reproduction rules.

## Installation
### Prerequisites
Ensure you have Python (3.x) installed. You also need to install Pygame:
```bash
pip install pygame
```

## How to Run
To start the simulation, run `main.py`:
```bash
python main.py
```
If you want to experiment with the AI-generated implementation, run:
```bash
python claude.py
```

## Game Rules
The Game of Life consists of a grid where each cell follows these rules:
1. A **live** cell with **fewer than two** live neighbors dies (underpopulation).
2. A **live** cell with **two or three** live neighbors survives.
3. A **live** cell with **more than three** live neighbors dies (overpopulation).
4. A **dead** cell with **exactly three** live neighbors becomes alive (reproduction).

## Features
- Customizable grid size and speed
- Randomized starting states
- User controls (pause/play, reset, adjust speed, etc.)
- Alternative AI-generated implementation (`claude.py`)

## Controls
- **G**: Generate inital population
- **Spacebar**: Pause/Resume
- **Mouse**: Modify the population manugally

## Contributing
Feel free to modify and extend the project! If you add new features, update this README accordingly.

## License
This project is open-source and available under the MIT License.

