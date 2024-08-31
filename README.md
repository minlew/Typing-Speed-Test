# Typing Speed Test App

## Description
This is a Python application that allows users to test and improve their typing speed. The app generates a random paragraph and measures how many characters the user can type correctly in 60 seconds.

### Features

* Random paragraph generation for each test.
* 60-second countdown timer.
* Real-time feedback on typing accuracy.
* End-of-test summary with characters per minute (CPM) score.
* Comparison to average adult typing speed and world record.

### Technologies
* Python

### Python Libs
* Tkinter
* Lorem

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Install [requirements](requirements.txt).
4. Run [script](main.py) in Python. 

## Usage
1. Click the "Start test" button to begin the typing test.
2. Type the displayed text as accurately and quickly as possible.
3. After 60 seconds, your results will be displayed, showing your CPM (Characters Per Minute) score.

## File Structure
* `main.py`: The main script containing the application code
* `logo.png`: The logo displayed on the start screen (should be in the same directory as `main.py`)

## Customization
* To change the test duration, modify the `count_down(60)` call in the `start_test()` function.
* You can adjust the font sizes and styles by modifying the relevant `font` parameters in the `create_text()` method calls.
