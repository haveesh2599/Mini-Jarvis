# 🤖 Mini Jarvis

Mini Jarvis is a Python-based voice assistant powered by Google's Gemini AI.

It listens to voice commands, converts speech into text, understands commands, performs basic Windows operations, and uses Gemini AI to answer questions that are not handled by built-in commands.

## ✨ Features

### 🎙️ Voice Interaction
- Voice command recognition using Speech Recognition
- Text-to-speech responses using `pyttsx3`
- Natural voice interaction with Jarvis

### 🧠 Gemini AI
- AI-powered question answering using Google Gemini
- Maintains a Gemini chat session for conversational interaction
- Automatically sends unrecognized commands/questions to Gemini

### 🌐 Web Controls
- Open YouTube
- Open Google
- Search Google using voice commands

### 💻 Application Controls
- Open Google Chrome
- Open Visual Studio Code
- Open Calculator
- Open Notepad
- Open File Explorer

### 🔊 System Volume Controls
- Set volume to a specific percentage
- Increase volume
- Decrease volume
- Volume up
- Volume down
- Mute volume
- Unmute volume
- Check current volume

### 🖥️ System Controls
- Take screenshots
- Lock the computer
- Get the current time
- Get the current date
- Exit Jarvis using voice commands

## 🛠️ Technologies Used

- Python
- Google Gemini AI
- Google Speech Recognition
- `pyttsx3` for text-to-speech
- `PyAutoGUI` for screenshots
- `pycaw` for Windows audio control
- `python-dotenv` for environment variables
- Windows system commands
- `webbrowser` for web automation

## 📁 Project Structure

```text
Mini-Jarvis/
│
├── jarvis.py
├── test_gemini.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

### File Description

| File | Description |
|------|-------------|
| `jarvis.py` | Main Jarvis voice assistant |
| `test_gemini.py` | Gemini API testing |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `LICENSE` | MIT License |
| `.gitignore` | Files excluded from Git |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/haveesh2599/Mini-Jarvis.git

2. Open the project directory
cd Mini-Jarvis

3. Create a virtual environment
python -m venv .venv

4. Activate the virtual environment
On Windows:
.venv\Scripts\activate

5. Install the required packages
pip install -r requirements.txt

🔑 Gemini API Setup
Mini Jarvis uses the Gemini API for AI-powered responses.
Create a .env file in the project directory:
GEMINI_API_KEY=your_api_key_here

Replace your_api_key_here with your own Gemini API key.
The application loads the API key from the environment instead of storing it directly in the Python source code.
⚠️ Never share or upload your Gemini API key publicly.

▶️ How to Run
Activate the virtual environment:
.venv\Scripts\activate

Then run:
python jarvis.py

Jarvis will greet you and begin listening for voice commands.
🎤 Example Commands
🧠 Ask Gemini AI
You can ask questions such as:
"What is artificial intelligence?"
"Explain machine learning"
"What is Python?"
"Tell me about neural networks"

Questions that do not match a built-in command are sent to Gemini AI for a response.
🌐 Websites
"Open YouTube"
"Go to YouTube"

"Open Google"
"Go to Google"

🔎 Google Search
"Search for Python tutorials"
"Search for artificial intelligence"
"Google latest Python features"

💻 Open Applications
"Open Chrome"
"Open VS Code"
"Open Visual Studio Code"
"Open Calculator"
"Open Notepad"
"Open File Explorer"
"Open Explorer"

🕐 Time and Date
"What time is it?"
"Tell me the time"
"Current time"

"What is the date?"
"Today's date"
"What day is it?"

🔊 Volume Controls
Set a specific volume:
"Set volume to 50"
"Set the volume to 75"
"Volume to 30"

Increase volume:
"Increase volume"
"Volume up"
"Increase volume by 10"
"Turn the volume up by 20"

Decrease volume:
"Decrease volume"
"Volume down"
"Decrease volume by 10"
"Turn the volume down by 20"

Mute and unmute:
"Mute"
"Mute volume"

"Unmute"
"Unmute volume"

Check the current volume:
"What is the volume?"
"What's the volume?"
"Current volume"
"Tell me the volume"

📸 Screenshot
"Take a screenshot"
"Take screenshot"
"Screenshot"
"Capture my screen"
"Capture the screen"

The screenshot is saved with a timestamped filename.
🔒 Lock Computer
"Lock my computer"
"Lock the computer"
"Lock computer"
"Lock my PC"
"Lock PC"

🛑 Exit Jarvis
"Stop Jarvis"
"Exit Jarvis"
"Quit Jarvis"
"Goodbye Jarvis"

🧠 How It Works
              🎙️ User Voice
                    │
                    ↓
           🗣️ Speech Recognition
                    │
                    ↓
             🧠 Command Processing
                    │
          ┌─────────┴─────────┐
          │                   │
          ↓                   ↓
   Built-in Command       AI Question
          │                   │
          ↓                   ↓
   Windows / Web        Gemini AI API
    Operations                │
          │                   │
          └─────────┬─────────┘
                    ↓
             🤖 Jarvis Response
                    │
                    ↓
             🔊 Text-to-Speech

Jarvis first checks whether the spoken command matches one of its built-in commands. If it does, Jarvis performs the corresponding action. Otherwise, the input is sent to Gemini AI and the response is spoken back to the user.
🔐 Security
The Gemini API key is stored in a .env file and is not included in the repository.
The following files are excluded using .gitignore:
.env
.venv/
__pycache__/

Never commit or share your API key publicly.
⚠️ Platform Compatibility
Mini Jarvis currently uses Windows-specific functionality for some system operations, including:
- Windows application launching
- Windows volume control
- Windows computer locking
Therefore, some features may not work correctly on macOS or Linux.
🚀 Future Improvements
- Wake-word detection
- More application controls
- More Windows system controls
- Music playback and control
- Weather information
- Reminders and alarms
- System information
- Conversation history management
- Graphical user interface
- Improved natural language command recognition
- Cross-platform support
👨‍💻 Author
Haveesh B A
B.Tech – Artificial Intelligence and Machine Learning
📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.