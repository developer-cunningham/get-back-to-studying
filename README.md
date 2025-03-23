# Get Back to Studying

This is a simple script that detects when you're using distracting apps (like Discord, YouTube, or Steam) and sends you a notification reminding you to study.

## Features
- Detects when certain applications are active.
- Sends a single notification per focus session.
- Supports multiple apps (configurable list).
- Lightweight and runs in the background.

## Installation
### Requirements
- Python 3.x
- Required libraries:
  ```sh
  pip install pygetwindow plyer
  ```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/developer-cunningham/get-back-to-studying.git
   ```
2. Navigate to the project directory and run the script:
   ```sh
   python main.py
   ```
3. If you open a tracked app (like Discord), a notification will remind you to get back to studying.

## Configuration
- Modify the `WATCHED_APPS` list in `main.py` to add or remove apps:
  ```python
  WATCHED_APPS = ["discord", "youtube", "steam"]
  ```
- Replace `sad.ico` with your own icon if desired.
- It's a pretty small script just read the code and make changes if you want!

## Contributing
Feel free to fork this repo and improve it! PRs are welcome.

## License
MIT License

