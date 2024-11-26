from flask import Flask, request, render_template_string
import pyautogui
import time
import threading

app = Flask(__name__)

# Global flag to control typing process
stop_typing_flag = False

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
        #stopBtn {
            display: none; /* Hide initially */
        }
    </style>
</head>
<body>
    <h1>Remote Auto Typer</h1>
    <form id="typingForm" method="POST" action="/type">
        <textarea name="text" placeholder="Paste your text here..." required></textarea>
        <br>
        <button type="submit" id="startBtn">Start Typing</button>
        <button type="button" id="stopBtn">Stop Typing</button>
    </form>

    <script>
        const startBtn = document.getElementById("startBtn");
        const stopBtn = document.getElementById("stopBtn");

        // Prevent form submission on clicking "Start Typing"
        startBtn.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent form submission
            
            const formData = new FormData(document.getElementById("typingForm"));

            // Show the stop button and hide the start button when typing starts
            stopBtn.style.display = "inline-block";
            startBtn.style.display = "none";

            // Send the text to the server using fetch()
            fetch("/type", {
                method: "POST",
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                console.log(data);
            })
            .catch(error => console.error("Error:", error));
        });

        // Stop Typing button functionality
        stopBtn.addEventListener("click", function() {
            fetch("/stop", { method: "POST" })
                .then(response => response.text())
                .then(data => {
                    console.log(data);
                    stopBtn.style.display = "none";  // Hide the stop button after stopping typing
                    startBtn.style.display = "inline";  // Show the start button again
                })
                .catch(error => console.error("Error:", error));
        });
    </script>
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
    global stop_typing_flag
    try:
        text = request.form.get("text", "")
        if text:
            stop_typing_flag = False  # Reset the stop flag when starting

            # Add a 5-second delay before typing starts
            time.sleep(5)
            # Split the text into lines for proper handling
            lines = text.split("\n")
            for line in lines:
                if stop_typing_flag:
                    return "Typing stopped.", 200

                parts = line.split("\t")  # Handle tabs if present
                for i, part in enumerate(parts):
                    if stop_typing_flag:
                        return "Typing stopped.", 200

                    # Type each part character by character
                    pyautogui.typewrite(part, interval=0.01)  # Adjust speed with interval
                    if i < len(parts) - 1:
                        pyautogui.press('tab')  # Simulate Tab key for tabs
                pyautogui.press('enter')  # Press Enter to start a new line

            return "Text successfully typed on your laptop!", 200
        return "No text provided!", 400
    except Exception as e:
        print(f"Error occurred: {e}")
        return f"Error: {e}", 500

@app.route("/stop", methods=["POST"])
def stop_typing():
    """Stop typing process."""
    global stop_typing_flag
    stop_typing_flag = True  # Set flag to stop typing
    return "Typing stopped!", 200

def run_server():
    """Run the Flask server."""
    try:
        app.run(host="0.0.0.0", port=5000)  # Accessible on the local network
    except Exception as e:
        print(f"Server failed to start: {e}")

# Start the server in a separate thread
if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    print("Server is running. Visit the URL on your phone or browser!")
    input("Press Enter to stop the server...\n")
