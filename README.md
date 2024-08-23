# SortiPy

SortiPy is a Python script that organizes files into folders based on their extensions. It saves user preferences using `pickle` files, allowing for customized sorting rules that persist across sessions.

## Features

- **Menu Interface**: A simple text-based menu for easy navigation and control.
- **Automatic Sorting**: Organizes files into folders by their extensions.
- **User Preferences**: Saves and loads user-defined sorting rules and target directories using `pickle`.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Error Handling**: Ensures smooth operation even if paths or files do not exist.

## Planned Features for Version 2

- **Graphical User Interface (GUI)**: A user-friendly interface to make it easier to set preferences and manage sorting rules.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/SortiPy.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SortiPy
    ```

3. Run the program:

    ```bash
    python menu.py
    ```

## Usage

1. **Menu Interface**: Navigate through the following options:

    - **Sort Files**: Automatically sort files into folders based on their extensions.
    - **Change Path**: Set a new directory path where files are to be sorted.
    - **Change Folder Properties**: 
        - Add or remove folders and their associated extensions.

2. **Function Descriptions**: Refer to the `functions_functionality.txt` file for detailed explanations of what each function in the script does.

## Contributing

Feel free to fork this repository, create new branches, and submit pull requests, any work on adding new functionality and a GUI would be really appreciated. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
