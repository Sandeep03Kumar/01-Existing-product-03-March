# hao-backprop-test

A minimal Flask web server built with Python 3. This tutorial project demonstrates basic HTTP routing with two endpoints that return plain-text responses. It is a direct rewrite of the original Express.js / Node.js server, preserving identical endpoint behavior.

## Prerequisites

- [Python](https://www.python.org/) 3.10 or higher (developed with Python 3.12.3)
- pip (included with Python)

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

This installs Flask and its transitive dependencies as declared in `requirements.txt`.

## Running the Server

Start the server directly with Python:

```bash
python app.py
```

The server binds to `http://127.0.0.1:3000/` and logs a confirmation message to the console:

```
Server running at http://127.0.0.1:3000/
```

## Available Endpoints

| Method | Path       | Response          | Content-Type | Status |
|--------|------------|-------------------|--------------|--------|
| GET    | `/`        | `Hello, World!\n` | `text/plain` | 200    |
| GET    | `/evening` | `Good evening`    | `text/plain` | 200    |

### Examples

```bash
curl http://127.0.0.1:3000/
# Hello, World!

curl http://127.0.0.1:3000/evening
# Good evening
```

## License

This project is licensed under the MIT License.
