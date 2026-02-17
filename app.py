"""
XKCD Comic Viewer - Starter Code
"""
from flask import Flask, render_template, request, redirect, url_for
import random
import requests

app = Flask(__name__)

XKCD_BASE_URL = "https://xkcd.com"


def get_latest_comic_number():
    """Return the latest comic number or None on failure."""
    latest = get_latest_comic()
    return latest.get('num') if latest else None

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
    latest_num = comic.get('num') if comic else None
    if comic:
        return render_template('index.html', comic=comic, latest_num=latest_num, error=None)
    else:
        return render_template('index.html', comic=None, latest_num=None,
                             error="Sorry, we couldn't fetch the comic right now. Please try again later.")


@app.route('/comic/<int:comic_num>')
def show_comic(comic_num):
    # Display a specific comic by number. Use this as a reference for implementing other features. example websiteUrl.com/comic/234
    # Validate comic number will pull back a comic
    if comic_num < 1:
        return render_template('index.html', comic=None, latest_num=get_latest_comic_number(),
                             error="Invalid comic number. Comics start at #1.")
    comic = get_comic_by_number(comic_num)
    latest_num = get_latest_comic_number()
    if comic:
        return render_template('index.html', comic=comic, latest_num=latest_num, error=None)
    else:
        return render_template('index.html', comic=None, latest_num=latest_num,
                             error=f"Comic #{comic_num} could not be found. It may not exist.")


@app.route('/random')
def random_comic():
    latest_num = get_latest_comic_number()
    if not latest_num:
        return render_template('index.html', comic=None, latest_num=None,
                             error="Unable to fetch the latest comic to choose a random one.")

    comic_num = random.randint(1, latest_num)
    comic = get_comic_by_number(comic_num)
    if comic:
        return render_template('index.html', comic=comic, latest_num=latest_num, error=None)
    return render_template('index.html', comic=None, latest_num=latest_num,
                         error="Could not fetch a random comic. Please try again.")


@app.route('/comic/<int:comic_num>/prev')
def previous_comic(comic_num):
    if comic_num <= 1:
        return render_template('index.html', comic=None, latest_num=None,
                             error="This is the first comic; there is no previous comic.")

    target = comic_num - 1
    while target >= 1:
        comic = get_comic_by_number(target)
        if comic:
            latest_num = get_latest_comic_number()
            return render_template('index.html', comic=comic, latest_num=latest_num, error=None)
        target -= 1

    return render_template('index.html', comic=None, latest_num=None,
                         error="Unable to locate a previous comic.")


@app.route('/comic/<int:comic_num>/next')
def next_comic(comic_num):
    latest_num = get_latest_comic_number()
    if not latest_num or comic_num >= latest_num:
        return render_template('index.html', comic=None, latest_num=latest_num,
                             error="This is the latest comic; there is no next comic yet.")

    target = comic_num + 1
    while target <= latest_num:
        comic = get_comic_by_number(target)
        if comic:
            return render_template('index.html', comic=comic, latest_num=latest_num, error=None)
        target += 1

    return render_template('index.html', comic=None, latest_num=latest_num,
                         error="Unable to locate the next comic.")


@app.route('/search', methods=['POST'])
def search_comic():
    try:
        comic_num = int(request.form.get('comic_num', '').strip())
    except (TypeError, ValueError, AttributeError):
        return render_template('index.html', comic=None, latest_num=get_latest_comic_number(),
                             error="Please enter a valid comic number.")

    return show_comic(comic_num)


@app.route('/recent')
@app.route('/recent/<int:count>')
def recent_comics(count=5):
    latest = get_latest_comic()
    if not latest:
        return render_template('index.html', comic=None, latest_num=None,
                             error="Unable to fetch recent comics right now.")

    latest_num = latest.get('num')
    count = max(1, min(count, 10))  # keep requests reasonable
    comics = []

    for num in range(latest_num, 0, -1):
        comic = get_comic_by_number(num)
        if comic:
            comics.append(comic)
        if len(comics) >= count:
            break

    primary = comics[0] if comics else None
    if primary:
        return render_template('index.html', comic=primary, latest_num=latest_num,
                               recent_comics=comics, error=None)
    return render_template('index.html', comic=None, latest_num=latest_num,
                         error="Unable to fetch recent comics right now.")

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
