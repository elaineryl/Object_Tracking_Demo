# Object Tracking Demo

This repository contains a demonstration of object tracking using OpenCV in Python. The demo showcases the use of various tracking algorithms available in OpenCV to track objects in a video.

## Features

- **Object Tracking**: Track an object in a video using user-defined bounding boxes.
- **Multiple Tracking Algorithms**: The demo supports various tracking algorithms provided by OpenCV.
- **Interactive UI**: Users can select the object to be tracked using a simple graphical interface.
- **Performance Metrics**: Display tracking performance metrics such as FPS.

## Prerequisites

- Python 3.x
- OpenCV 4.x (with `opencv-contrib-python` for additional tracking algorithms)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/micahkepe/Object_Tracking_Demo.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd Object_Tracking_Demo
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the demo script:
   ```bash
   python3 Demo.py
   ```

2. An interface will open displaying the first frame of the video. Select the object you want to track by drawing a bounding box around it.

3. The tracker will then track the object throughout the video, displaying the tracked object with a bounding box.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


