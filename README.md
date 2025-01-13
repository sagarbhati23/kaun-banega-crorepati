# KBC GUI Game

This project is a graphical user interface (GUI) implementation of the popular quiz game "Kaun Banega Crorepati" (KBC). The game allows users to answer questions and win virtual prizes based on their knowledge.

## Project Structure

```
kbc-gui
├── src
│   ├── kbc.py          # Core logic of the KBC game
│   ├── gui.py          # GUI implementation using a framework
│   └── assets
│       └── styles.css  # Styling for the GUI components
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kbc-gui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the KBC game, execute the following command:
```
python src/gui.py
```

This will launch the GUI application where you can start playing the game.

## Dependencies

The project requires the following libraries:
- [Tkinter](https://docs.python.org/3/library/tkinter.html) or [PyQt](https://www.riverbankcomputing.com/software/pyqt/intro) (for GUI)
- Any other libraries specified in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

