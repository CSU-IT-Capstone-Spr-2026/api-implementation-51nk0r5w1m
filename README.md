[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/zN2AskmG)

# XKCD Comic Viewer

A Flask web application that lets users browse XKCD webcomics using the XKCD JSON API. Users can view the latest comic, navigate between comics with previous/next buttons, jump to a random comic, search for a specific comic by number, and browse a grid of the most recent comics.

## Features Implemented

Check off the features you implemented (must have at least 4 and 2 are implemeted for you already):

- [X] Feature #1: Display the Latest Comic
- [X] Feature #2: Display a Specific Comic by Number
- [X] Feature #3: Random Comic Button
- [X] Feature #4: Navigation (Previous/Next)
- [X] Feature #5: Search by Comic Number Form
- [X] Feature #6: Display Multiple Recent Comics

## Technologies Used

- Python 3.8+
- Flask 3.0.0
- Requests 2.31.0
- XKCD API

## Installation and Setup

### Prerequisites

- Python 3.8 or higher installed
- pip (Python package manager)

### Steps to Run

1. Clone or download this repository

2. Navigate to the project directory in your terminal:

```sh
cd projectName
```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

4. Run the application:

```sh
python app.py
```

5. Open your web browser and go to:

```sh
http://localhost:5000
```

## Usage

- **Latest Comic**: The home page automatically displays the most recent XKCD comic.
- **Random Comic**: Click the "Random Comic" button in the header or the "Random" button below any comic to load a random comic.
- **Navigate Comics**: Use the "Previous" and "Next" buttons below each comic to browse through comics in order.
- **Search**: Enter a comic number in the search box below the comic and click "Go" to jump to that specific comic.
- **Recent Comics**: Click "Recent Comics" in the header to see a grid of the 5 most recent comics with thumbnails.

## Screenshots

- [Latest Comic View](screenshots/XKCD%20Comic%20Viewer.pdf)
- [Random Comic View](screenshots/XKCD%20Rand%20Comic%20Viewer.pdf)
- [Recent Comics View](screenshots/XKCD%20Recent%20Comic%20Viewer.pdf)

## API Endpoints Used

- `GET /info.0.json` - Fetches the latest comic
- `GET /{comic_number}/info.0.json` - Fetches a specific comic by number

## Challenges and Solutions

One challenge was handling navigation between comics. Because there are gaps in XKCD's numbering, simply subtracting or adding one to the current comic number does not always land on a valid comic. I solved this by implementing a loop that tries the next number in sequence and skips over any 404 responses until it finds a valid comic.

Another challenge was keeping the UI responsive while fetching multiple comics for the recent comics page. Each comic requires a separate API request since the XKCD API only returns one comic at a time. I limited the count to a reasonable maximum and iterated backwards from the latest comic number to collect the results.

Working on this project taught me how REST APIs work in practice. I learned how to make GET requests, parse JSON responses, and handle common HTTP status codes like 200 and 404. I also learned the importance of error handling since network requests can fail for many reasons, and a good application needs to show helpful messages instead of crashing.

## Future Improvements

- Add a favorites system so users can save and revisit their favorite comics
- Add caching to avoid re-fetching comics that were already loaded
- Add a search-by-title feature using a local index of comic titles

## Author

Carley Fant // 51nk0r5w1m