"""
NJAM index (main) view.

URLs include:
/
"""
from calendar import c
import flask
import closet


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
              " WHERE location =" + location)
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
def index():
    """Display / route."""

    context = {}
    return flask.render_template("index.html.jinja", **context)


@closet.app.route('/location_page', methods=['GET'])
def location_page():
    """Display /locations route."""

    # Connect to database
    connection = closet.model.get_db()
    cur = connection.execute(
        "SELECT * "
        "FROM locations"
    )
    locations = cur.fetchall()

    for location in locations:
        percent_capacity = location["capacity"]/location["max_capacity"]
        location["percent_capacity"] = u"{0:.0f}".format(
            percent_capacity * 100)

    context = {"locations": locations}
    return flask.render_template("location_page.html.jinja", **context)
