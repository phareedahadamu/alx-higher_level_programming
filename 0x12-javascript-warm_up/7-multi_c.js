#!/usr/bin/node
/* prints 'C is fun' x number of times
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You can use only two console.log
 * You must use a loop (while, for, etc.)
 */
let i = 0;
const myVar = Number(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  while (i < myVar) {
    console.log('C is fun');
    i++;
  }
}
