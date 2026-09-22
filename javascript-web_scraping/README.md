# JavaScript - Web Scraping

## Description

A set of small Node.js scripts covering file I/O (`fs`) and HTTP requests (`request`), used to read/write files and pull data from a few public APIs: a status-code check, the Star Wars API (SWAPI), and the JSONPlaceholder todos API.

## Requirements

- All scripts are interpreted/compiled on Ubuntu using `Node.js 22.x`
- All files end with a new line
- All scripts must be executable
- The first line of all scripts is exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `js` extension
- All code is verified against `semistandard` using the following command: `semistandard *.js`
- `var` is never used — only `const`/`let`
- The `request` module must be installed and used for every task involving an HTTP call: `npm install request`

## Tasks

| File | Description |
| --- | --- |
| `0-readme.js` | Reads and prints the content of a file (UTF-8), or the error object if it fails |
| `1-writeme.js` | Writes a string to a file (UTF-8), printing the error object if it fails |
| `2-statuscode.js` | Prints the HTTP status code of a GET request to a given URL |
| `3-starwars_title.js` | Prints the title of a Star Wars movie by its SWAPI episode ID |
| `4-starwars_count.js` | Counts how many films feature the character Wedge Antilles (people ID 18) |
| `5-request_store.js` | Fetches a URL's body and writes it to a file |
| `6-completed_tasks.js` | Counts completed todos per user ID from the JSONPlaceholder API |

## Usage

```bash
./<script_name>.js [arguments]
```

Example:

```bash
$ ./2-statuscode.js https://alu-intranet.hbtn.io/status
code: 200
```

## Author

Quentin Kayitare
