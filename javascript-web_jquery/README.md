# JavaScript - Web jQuery

## Description

Small browser scripts covering DOM manipulation with vanilla JavaScript and with jQuery: selecting elements, changing styles and classes, handling click events, building lists dynamically, and fetching data from external APIs (SWAPI and a translation API) with `$.get`.

Unlike the Node.js projects in this repo, these scripts run in the browser and are meant to be loaded from the corresponding `-main.html` test file given in each task — there's no automated checker here, each task is reviewed manually by loading the HTML file and checking the resulting behavior.

## Requirements

- All scripts are executed in a browser, loaded via a `<script>` tag from an HTML file
- Tasks 1–9 must use the jQuery API and must NOT use `document.querySelector`
- Task 0 must use `document.querySelector` and must NOT use jQuery
- `var` is never used — only `const`/`let`/function expressions

## Tasks

| File | Description |
| --- | --- |
| `0-script.js` | Colors the `<header>` red using `document.querySelector` |
| `1-script.js` | Colors the `<header>` red using jQuery |
| `2-script.js` | Colors the `<header>` red on click of `DIV#red_header` |
| `3-script.js` | Adds the `red` class to `<header>` on click of `DIV#red_header` |
| `4-script.js` | Toggles the `<header>` class between `red` and `green` on click of `DIV#toggle_header` |
| `5-script.js` | Adds a new `<li>Item</li>` to `UL.my_list` on click of `DIV#add_item` |
| `6-script.js` | Updates the `<header>` text to `New Header!!!` on click of `DIV#update_header` |
| `7-script.js` | Fetches a Star Wars character's name from SWAPI and displays it in `DIV#character` |
| `8-script.js` | Fetches all Star Wars movie titles from SWAPI and lists them in `UL#list_movies` |
| `9-script.js` | Fetches a translation of "hello" and displays it in `DIV#hello`, safe to load from `<head>` |

## Usage

Each script is loaded from its matching `-main.html` file, e.g.:

```html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
...
<script type="text/javascript" src="2-script.js"></script>
```

Open the HTML file directly in a browser to test the behavior described in each task.

## Author

Quentin Kayitare
