"""
Flask web server with Hello World and Good Evening endpoints.

A minimal Flask application that serves two plain-text HTTP GET endpoints,
replicating the behavior of the original Express.js Node.js server.
"""

from flask import Flask, Response

# Application instance
app = Flask(__name__)

# Server configuration — matches the original Node.js server binding
HOSTNAME = '127.0.0.1'
PORT = 3000


@app.route('/', methods=['GET'])
def hello_world():
    """Return a plain-text 'Hello, World!' greeting with a trailing newline.

    This endpoint preserves the exact response body, content type, and status
    code of the original Node.js ``http.createServer()`` handler that was later
    migrated to an Express.js ``GET /`` route.

    Returns:
        Response: HTTP 200 with ``text/plain`` body ``Hello, World!\\n``.
    """
    return Response('Hello, World!\n', status=200, content_type='text/plain')


@app.route('/evening', methods=['GET'])
def good_evening():
    """Return a plain-text 'Good evening' greeting.

    This endpoint matches the Express.js ``GET /evening`` route that was added
    as part of the Express.js integration.

    Returns:
        Response: HTTP 200 with ``text/plain`` body ``Good evening``.
    """
    return Response('Good evening', status=200, content_type='text/plain')


if __name__ == '__main__':
    # Mirror the original Node.js startup log message
    print(f'Server running at http://{HOSTNAME}:{PORT}/')
    app.run(host=HOSTNAME, port=PORT)
