Flask Joke App

Overview

This is a simple Flask web application that generates and displays programming jokes using the pyjokes library. You can either get a single joke at a time or fetch multiple jokes at once.

Prerequisites

Before running this project, ensure that you have:

Python installed (version 3.x recommended)

Flask library installed

pyjokes library installed

Installation & Setup

1. Clone or Download the Project

If you have downloaded the script, move to the folder where it is saved.

2. Install Required Libraries

Open a terminal and run the following command:

pip install flask pyjokes

This will install Flask and pyjokes, which are necessary for running the application.

Running the Application

1. Start the Flask Server

Run the following command in your terminal (ensure you're in the project directory):

python filename.py

Replace filename.py with the actual filename containing the script.

2. Open in Browser

After running the above command, Flask will start a development server. You should see an output similar to:

Running on http://127.0.0.1:5000/

Now open a web browser and enter one of the following URLs:

For a single joke:

http://127.0.0.1:5000/single_joke

This will fetch and display one joke at a time.

For multiple jokes:

http://127.0.0.1:5000/multiple_jokes

This will fetch multiple jokes and display them.

File Structure

app.py (or your chosen filename): Contains the main Flask app

templates/input.html: Required for rendering jokes (Ensure you have this file, or create it as needed.)

Notes

The app runs in debug mode, meaning you can see errors in real-time.

The page loads jokes dynamically using Flask's templating feature.

Troubleshooting

If you encounter a ModuleNotFoundError, make sure you have installed Flask and pyjokes using pip.

Ensure input.html exists in the templates folder. You can create a simple HTML file that displays jokes inside a loop.

Future Improvements

Adding a button to fetch new jokes without refreshing the page.

Enhancing the UI using CSS.

Allowing users to select different joke categories.

Enjoy coding and have fun with jokes! 🎉

