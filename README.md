# Remote-auto-typer

# Remote Auto Typer

A Python Flask application that automates typing on a local machine using a web-based interface. It allows users to input text remotely and simulates typing it line by line, handling tabs and line breaks.

## Features
- Type text remotely using a web browser.
- Handles tabs (`\t`) and new lines (`\n`) automatically.
- Start and stop typing dynamically from the interface.
- Adjustable typing speed for realistic typing simulation.

## Prerequisites
- Python 3.x
- Flask
- PyAutoGUI
- Other required libraries (see [requirements.txt](./requirements.txt))

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/remote-auto-typer.git
    cd remote-auto-typer
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python server.py
    ```

4. Access the web interface from you remote device at:
    ```
    http://<your_local_ip>:5000/
    ```
    

## Usage
1. Paste the text into the text area.
2. Click "Start Typing" and focus on the desired window.
3. To stop typing mid-process, click "Stop Typing."

## Security Considerations
- Only run on trusted networks.
- Avoid simultaneous use of clipboard-dependent applications while running this program.

## Contributions
Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.

<!-- ## License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details. -->
