"""
Closet upload view.

URLs include:
/upload/<filename>
"""
import os
import flask
import closet


@closet.app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Upload file."""
    # If an unauthenticated user attempts
    # to access an uploaded file, abort(403),
    # regardless of whether the file exists.
    # not done
    # If an authenticated user attempts
    # to access a file that does not exist, abort(404).
    if 'username' not in flask.session or flask.session['username'] == "":
        flask.abort(403)
    if not os.path.exists(
            closet.app.config['UPLOAD_FOLDER']/filename):
        flask.abort(404)
    return flask.send_from_directory(
        closet.app.config['UPLOAD_FOLDER'], filename)
