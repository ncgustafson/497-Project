"""
NJAM index (main) view.

URLs include:
/
"""
import flask
import arrow
import closet
import uuid
import pathlib

@closet.app.route('/locations/')
def get_locations():
    """Return post on postid."""
    arguments = flask.request.args
    connection = closet.model.get_db()
    if len(arguments) != 0:
        location = arguments.get('location')
        capacity = arguments.get('capacity')

        print("UPDATE locations "
            "SET capacity=" + capacity +
            " WHERE location =" + location )
        cur = connection.execute(
            "UPDATE locations "
            "SET capacity=" + capacity +
            " WHERE location ='" + location + "'"           
        )
    
    cur = connection.execute(
        "SELECT * "
        "FROM locations"
    )
    locations = cur.fetchall()
    for location in locations:
        percent_capacity = location["capacity"]/location["max_capacity"]
        location["percent_capacity"] = percent_capacity * 100
    print(locations)
    context = {
        "locations": locations        
    }
    return flask.jsonify(**context)

@closet.app.route('/', methods=['GET'])
def show_index():
    """Display / route."""
    """Return post on postid."""

     # Connect to database
    connection = closet.model.get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM locations"
    )

    locations = cur.fetchall()

    for location in locations:
        percent_capacity = location["capacity"]/location["max_capacity"]
        location["percent_capacity"] = percent_capacity * 100

    context = {"locations": locations}
    return flask.render_template("index.html", **context)

