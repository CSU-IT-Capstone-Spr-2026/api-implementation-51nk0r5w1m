"""
XKCD Comic Viewer - Starter Code
"""
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

XKCD_BASE_URL = "https://xkcd.com"

def get_latest_comic():
    # Fetch the most recent XKCD comic from the API and returns dict: Comic data if successful, None if there's an error
    try:
        response = requests.get(f"{XKCD_BASE_URL}/info.0.json")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


def get_comic_by_number(comic_num):
    # Fetch a specific XKCD comic by its number. Takes argument comic_num (int): The comic number to fetch
    try:
        response = requests.get(f"{XKCD_BASE_URL}/{comic_num}/info.0.json")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Comic #{comic_num} not found")
            return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


@app.route('/')
def index():
    #Home page - displays the latest XKCD comic. Implements Feature #1: Display the Latest Comic
    # Fetch the latest comic and if successful, render the template with comic data else show an error
    comic = get_latest_comic()
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None, 
                             error="Sorry, we couldn't fetch the comic right now. Please try again later.")


@app.route('/comic/<int:comic_num>')
def show_comic(comic_num):
    # Display a specific comic by number. Use this as a reference for implementing other features. example websiteUrl.com/comic/234
    # Validate comic number will pull back a comic
    if comic_num < 1 or comic_num > 3200:
        return render_template('index.html', comic=None,
                             error="Invalid comic number. Comics start at #1.")
    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, error=None)
    else:
        return render_template('index.html', comic=None,
                             error=f"Comic #{comic_num} could not be found. It may not exist.")


# TODO: Add more routes here for the other features you choose to implement
# Feature #3: Random Comic
# Feature #4: Navigation (Previous/Next)
# Feature #5: Search Form
# Feature #6: Display Multiple Recent Comics

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=5000)