#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const [, , x, y] = process.argv;
console.log(add(parseInt(x, 10), parseInt(y, 10)));
