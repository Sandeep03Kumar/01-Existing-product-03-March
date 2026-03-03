# hao-backprop-test

A minimal Express.js web server built with Node.js. This tutorial project demonstrates basic HTTP routing with two endpoints that return plain-text responses.

## Prerequisites

- [Node.js](https://nodejs.org/) v18 or higher (developed with Node.js 20.20.0)
- npm (included with Node.js)

## Installation

Clone the repository and install dependencies:

```bash
npm install
```

This installs Express.js and its transitive dependencies as declared in `package.json`.

## Running the Server

Start the server using npm:

```bash
npm start
```

Or run it directly with Node.js:

```bash
node server.js
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
