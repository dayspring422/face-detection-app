# Face Detection App

This project is a comprehensive face detection application that uses OpenCV to detect faces in real-time. The application provides three different interfaces for face detection: a command-line interface (CLI), a graphical user interface (GUI) using PyQt, and a web application using Flask.

## Features

- **Real-time Face Detection**: Capture video from the webcam and detect faces in real-time.
- **Command-Line Interface (CLI)**: Simple and straightforward face detection in a video window.
- **Graphical User Interface (GUI)**: Interactive face detection using PyQt, offering a more user-friendly experience.
- **Web Application**: Stream video with face detection over a web interface using Flask.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Flask
- PyQt5


Certainly! Here's the README file content formatted in a code block style:

markdown
Copy code
# Face Detection App

This project is a comprehensive face detection application that uses OpenCV to detect faces in real-time. The application provides three different interfaces for face detection: a command-line interface (CLI), a graphical user interface (GUI) using PyQt, and a web application using Flask.

## Features

- **Real-time Face Detection**: Capture video from the webcam and detect faces in real-time.
- **Command-Line Interface (CLI)**: Simple and straightforward face detection in a video window.
- **Graphical User Interface (GUI)**: Interactive face detection using PyQt, offering a more user-friendly experience.
- **Web Application**: Stream video with face detection over a web interface using Flask.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Flask
- PyQt5

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/face-detection-app.git
   cd face-detection-app
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Command-Line Interface (CLI)
Run the CLI application:

bash
Copy code
python face_detection.py
A window will open showing the video feed from your webcam with detected faces highlighted by rectangles. Press 'q' to quit the application.

Graphical User Interface (GUI)
Run the GUI application:

bash
Copy code
python main.py gui
A PyQt window will open displaying the video feed with face detection.

Web Application
Run the Flask web application:

bash
Copy code
python main.py
Open your web browser and navigate to http://127.0.0.1:5000/ to view the video stream with face detection.

Code Overview
face_detection.py
A simple CLI application that captures video from the webcam, detects faces, and displays the video feed with rectangles drawn around detected faces.

gui_app.py
A PyQt-based GUI application for real-time face detection. It provides a more interactive user interface with a video feed showing detected faces.

app.py
A Flask-based web application that streams video with face detection. It captures frames from the webcam, processes them for face detection, and streams the processed video to a web page.

templates/index.html
An HTML template for the Flask web application that displays the video feed with face detection.

main.py
A script to run either the GUI or web application based on command-line arguments.








