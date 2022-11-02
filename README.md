# Virtual_Closet
493 Final Project

## How to run
### For Linux and Windows 10 Subsystem for Linux
`sudo apt-get install sqlite3 curl`
### For MACOS
`brew install sqlite3 curl`

Open a python virtual environment, but make sure you are in the correct directory.
`pwd` should return `/Virtual_Closet/` at the very end. Then run:

- `source env/bin/activate`
- `pip install -r requirements.txt`
- `./bin/database reset`
- `./bin/run`
And please make your way to the localhost provided in the terminal.

## Contributions
Team Members
### Nicholas
- Added additional article of clothing form.
- Including adding each piece of clothing to databases, and displaying them
- Wrote closet/ laundry basket python functions
- Implemented python functions to send clothes to and from closet/laundry
### Zain
- Styled the outfit picker page
- Implemented the functionality of the apply button
- Positioned all the images properly on the outfit page
- Positioned shirt and pant images on the person shown in the outfit page when clothes are applied
### Rahul
- Added prop images and styled
- Added slider buttons
- Added background
- Added help text
- Added html formatting
- Added js images functionality for sliding buttons
- Added redirecting of images on page
### Kyle
- Worked on `outfit.html`
- Added help text and instructions
- Added html and css formatting 
- Implemented functionality for outfit.html features
### Hubert
- Created SQL and SQLite3 Functionality
- Worked solely on the Homepage
- Created Flask App "Closet"
- Worked on connecting `index.html` and `outfit.html`
- Added functionality for the carousel on the Homepage
- Implemented python functions to send clothes to and from closet/laundry
- Wrote the scripts and the instructions on the README.md
