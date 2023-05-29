# ZoomAutomation Project

> :sparkles: **Note:** This project is designed for Windows.

This project allows for automatic joining and leaving of Zoom meetings using the provided `main.py` script and the functions included in `zoomFuncs.py`. You will need to add your own Zoom meeting codes and passwords to make it work.

## Getting Started

To get started with the ZoomAutomation project, follow these steps:

1. Clone the project repository:

   ```bash
   git clone https://github.com/your-username/ZoomAutomation.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Open `main.py` and update the following variables with your Zoom meeting information:

   ```python
   classCode = "YOUR_MEETING_CODE"
   classPass = "YOUR_MEETING_PASSWORD"
   ```

   Add more meeting codes and passwords as needed.

4. Run the `main.py` script to start the ZoomAutomation:

   ```bash
   python main.py
   ```

## Project Structure

The project structure is as follows:

```
ZoomAutomation/
├── main.py
├── zoomFuncs.py
└── sourceImages/
    └── ...
```

- `main.py`: This is the main script that handles the automation logic and uses functions from `zoomFuncs.py`.
- `zoomFuncs.py`: This file contains the implementation of functions for joining and leaving Zoom meetings.

## Dependencies

The following dependencies are required for the project:

- Python 3.x
- `os` library: Used for interacting with the operating system.
- `time` library: Used for time-related operations.
- `py32gui` library: Used for managing windows.
- `re` library: Used for regular expression operations.
- `PIL` library: Used for image processing.
- `functools` library: Used for higher-order functions and function composition.
- `schedule` library: Used for scheduling tasks.
- `time` library: Used for time-related operations.

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```
