# JavaScript - Warm up

## Description

A set of introductory JavaScript scripts covering the language fundamentals: variables, command-line arguments, type conversion, loops, functions, recursion, objects, and modules. Every script is run directly with Node.js and follows the `semistandard` style guide (2-space indentation, single quotes, semicolons, no `var`).

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
| `0-javascript_is_amazing.js` | Prints `JavaScript is amazing` using a constant |
| `1-multi_languages.js` | Prints 3 fixed lines |
| `2-arguments.js` | Prints a message depending on the number of arguments passed |
| `3-value_argument.js` | Prints the first argument, without using `.length` |
| `4-concat.js` | Prints two arguments in the format `<a> is <b>` |
| `5-to_integer.js` | Converts the first argument to an integer, without `try`/`catch` |
| `6-multi_languages_loop.js` | Prints 3 languages using an array, a loop, and a single `console.log` |
| `7-multi_c.js` | Prints `C is fun` `x` times, using a loop and only two `console.log` calls |
| `8-square.js` | Prints a square of `X` characters based on the given size |
| `9-add.js` | Adds two integers using a function `add(a, b)` |
| `10-factorial.js` | Computes a factorial recursively |
| `11-second_biggest.js` | Finds the second biggest integer among the arguments |
| `12-object.js` | Mutates an object's property while keeping it declared as `const` |
| `13-add.js` / `13-main.js` | Exports an `add` function from a module and uses it in another script |

## Usage

```bash
./<script_name>.js [arguments]
```

Example:

```bash
$ ./9-add.js 13 89
102
```

## Author

Quentin Kayitare
