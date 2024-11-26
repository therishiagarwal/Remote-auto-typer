from flask import Flask, request, render_template_string
import pyautogui
import pyperclip
import time
import threading

app = Flask(__name__)

# HTML template for the webpage
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remote Auto Typer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            text-align: center;
            background-color: #f4f4f4;
        }
        textarea {
            width: 90%;
            max-width: 600px;
            height: 150px;
            margin: 20px auto;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: block;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Remote Auto Typer</h1>
    <form method="POST" action="/type">
        <textarea name="text" placeholder="Paste your text here..." required></textarea>
        <br>
        <button type="submit">Start Typing</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    """Render the input form."""
    return render_template_string(HTML_TEMPLATE)

@app.route("/type", methods=["POST"])
def auto_type():
    """Handle text input and start typing."""
    try:
        text = request.form.get("text", "")
        if text:
            # Add a 5-second delay before typing starts
            time.sleep(5)
            # Split the text into lines for proper handling
            lines = text.split("\n")
            for line in lines:
                parts = line.split("\t")  # Handle tabs if present
                for i, part in enumerate(parts):
                    # Type each part character by character
                    pyautogui.typewrite(part, interval=0.01)  # Simulate typing (adjust speed with interval)
                    if i < len(parts) - 1:
                        pyautogui.press('tab')  # Simulate Tab key for tabs
                pyautogui.press('enter')  # Press Enter to start a new line
            return "Text successfully typed on your laptop!", 200
        return "No text provided!", 400
    except Exception as e:
        print(f"Error occurred: {e}")
        return f"Error: {e}", 500


def run_server():
    """Run the Flask server."""
    try:
        app.run(host="0.0.0.0", port=5000)  # Accessible on the local network
    except Exception as e:
        print(f"Server failed to start: {e}")

# Start the server
if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    print("Server is running. Visit the URL on your phone or browser!")
    input("Press Enter to stop the server...\n")
