#!/usr/bin/node
/* prints a square.
 * The first argument is the size of the square.
 * If the first argument can’t be converted to an integer, print “Missing size”.
 * You must use the character X to print the square.
 * You must use console.log(...) to print all output.
 * You are not allowed to use var.
 * You must use a loop (while, for, etc.)
 */
let i = 0;
let j = 0;
let str = '';
const myVar = Number(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  while (i < myVar) {
    str = str + 'X';
    i++;
  }
  while (j < myVar) {
    console.log(str);
    j++;
  }
}
