# JavaScript - Objects, Scopes and Closures

## Description

This project covers JavaScript's `class` syntax, inheritance with `extends`/`super`, closures, and a handful of array/function utilities. It builds a small `Rectangle`/`Square` class hierarchy step by step, then adds standalone utility functions that rely on closures and functional patterns.

## Requirements

- All scripts are interpreted/compiled on Ubuntu using `Node.js 22.x`
- All files end with a new line
- All scripts must be executable
- The first line of all scripts is exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `js` extension
- All code is verified against `semistandard` using the following command: `semistandard *.js`
- `var` is never used — only `const`/`let`

## Tasks

| File | Description |
| --- | --- |
| `0-rectangle.js` | An empty `Rectangle` class |
| `1-rectangle.js` | `Rectangle` with a `width`/`height` constructor, no validation |
| `2-rectangle.js` | `Rectangle` that stays empty if `w`/`h` isn't a positive integer |
| `3-rectangle.js` | Adds a `print()` method that draws the rectangle with `X` |
| `4-rectangle.js` | Adds `rotate()` (swap width/height) and `double()` (multiply both by 2) |
| `5-square.js` | `Square` extends `Rectangle` (4-rectangle.js), constructor takes a single `size` |
| `6-square.js` | `Square` extends `Square` (5-square.js), adds `charPrint(c)` with a custom fill character |
| `7-occurrences.js` | Counts how many times a value appears in a list |
| `8-esrever.js` | Reverses a list without using `.reverse()` |
| `9-logme.js` | Uses a closure to track and print how many arguments have been logged so far |
| `10-converter.js` | Returns a function that converts a base-10 number into another base, with no imports or extra variable declarations |

## Usage

```bash
./<script_name>.js
```

Each file exports its class or function via `module.exports`/`exports`, so they're meant to be required from a corresponding `-main.js` test file, e.g.:

```bash
$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();
```

## Author

Quentin Kayitare
