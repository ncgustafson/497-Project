"""
Insta485 index (main) view.

URLs include:
/
"""
import flask
import arrow
import closet
import uuid
import pathlib

@closet.app.route('/', methods=['GET'])
def show_index():
    """Display / route."""
    # Connect to database
    connection = closet.model.get_db()

    ## clean clothes start ##
    cur = connection.execute(
        "SELECT * "
        "FROM clothing"
    )
    clothes = cur.fetchall()
    categories = []
    clean_category_count = {}
    for cloth in clothes:
        if cloth['cloth_type'] not in categories:
            categories.append(cloth['cloth_type'])
        if cloth['cloth_type'] not in clean_category_count:
            clean_category_count[cloth['cloth_type']] = 1
        else:
            clean_category_count[cloth['cloth_type']] += 1
    for category in categories:
        if category not in clean_category_count:
            clean_category_count[category] = 0
    print(clean_category_count)
    ## clean clothes end ##
    ########################
    ## dirty laundry start ##
    cur = connection.execute(
        "SELECT * "
        "FROM laundry"
    )
    laundry = cur.fetchall()
    dirty_category_count = {}
    for cloth in laundry:
        if cloth['cloth_type'] not in categories:
            categories.append(cloth['cloth_type'])
        if cloth['cloth_type'] not in dirty_category_count:
            dirty_category_count[cloth['cloth_type']] = 1
        else:
            dirty_category_count[cloth['cloth_type']] += 1
    for category in categories:
        if category not in dirty_category_count:
            dirty_category_count[category] = 0
    print(dirty_category_count)
    ## dirty laundry end ##
    context = {"clothing": clothes, "categories": categories, "clean_count": clean_category_count,
    "laundry": laundry, "dirty_count": dirty_category_count}
    return flask.render_template("index.html", **context)

@closet.app.route('/', methods=['POST'])
def new_clothes():
    """Display / route."""
    connection = closet.model.get_db()
    fileobj = flask.request.files["file"]

    filename = fileobj.filename

    uuid_basename = "{stem}{suffix}".format(
        stem=uuid.uuid4().hex,
        suffix=pathlib.Path(filename).suffix
    )

    path = closet.app.config["UPLOAD_FOLDER"]/pathlib.Path(filename)
    fileobj.save(path)

    clothing_type = flask.request.form['clothing_type']
    print(clothing_type)
    
    cur = connection.execute(
        "SELECT * "
        "FROM clothing " 
        "WHERE cloth_type == ?",
        (clothing_type, ) 
    )

    num_of_clothes = cur.fetchall()
    print(num_of_clothes)
    num_of_clothes = len(num_of_clothes)

    cur = connection.execute(
        "SELECT * "
        "FROM clothing "
    )

    id = cur.fetchall()
    id = len(id)
    cur = connection.execute(
        "SELECT * "
        "FROM laundry "
    )
    dirty_id = cur.fetchall()
    dirty_id = len(dirty_id)
    id += dirty_id + 1
    cur = connection.execute(
               "INSERT INTO clothing(id, cloth_type, filename) "
               "VALUES('" + str(id) + "', '"
              +  clothing_type + "', '" + filename + "');"
    )
#
  #          INSERT INTO clothing(id, cloth_type, filename)
 #   VALUES('1', 'sweater', 'sweater1.jpg');
    return flask.redirect('/')



@closet.app.route('/make_laundry/', methods=['POST'])
def make_laundry():
    connection = closet.model.get_db()
    filename = flask.request.form['filename']
    cur = connection.execute(
        "SELECT * "
        "FROM clothing "
        "WHERE filename == ? ",
        (filename, )
    )
    current_stuff = cur.fetchall()[0]
    print(current_stuff)
    cur = connection.execute(
        "INSERT INTO laundry(id, cloth_type, filename) "
        "VALUES (?, ?, ?) ",
        (current_stuff['id'], current_stuff['cloth_type'], current_stuff['filename'], )
    )
    cur = connection.execute(
        "DELETE "
        "FROM clothing "
        "WHERE filename == ? ",
        (filename, )
    )
    return flask.redirect('/')

@closet.app.route('/make_clean/', methods=['POST'])
def make_clean():
    connection = closet.model.get_db()
    filename = flask.request.form['filename']
    cur = connection.execute(
        "SELECT * "
        "FROM laundry "
        "WHERE filename == ? ",
        (filename, )
    )
    current_stuff = cur.fetchall()[0]
    print(current_stuff)
    cur = connection.execute(
        "INSERT INTO clothing(id, cloth_type, filename) "
        "VALUES (?, ?, ?) ",
        (current_stuff['id'], current_stuff['cloth_type'], current_stuff['filename'], )
    )
    cur = connection.execute(
        "DELETE "
        "FROM laundry "
        "WHERE filename == ? ",
        (filename, )
    )
    return flask.redirect('/')



@closet.app.route('/move_laundry/', methods=['POST'])
def move_laundry():
    connection = closet.model.get_db()

    cur = connection.execute(
        "SELECT * "
        "FROM laundry "
    )
    laundry = cur.fetchall()

    for cloth in laundry:
        cur = connection.execute(
            "INSERT INTO clothing(id, cloth_type, filename) "
            "VALUES (?, ?, ?) ",
            (cloth['id'], cloth['cloth_type'], cloth['filename'], )
        )

    cur = connection.execute(
        "DELETE "
        "FROM laundry"
    )
    return flask.redirect('/')