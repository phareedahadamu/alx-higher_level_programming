#!/usr/bin/node
/* searches the second biggest integer in the list of arguments.
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
let first;
let second;
let i = 3;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  first = Number(process.argv[2]);
  second = Number(process.argv[3]);
  while (i < process.argv.length) {
    if (Number(process.argv[i]) > first) {
      second = first;
      first = Number(process.argv[i]);
    } else {
      if (Number(process.argv[i]) > second) {
        second = Number(process.argv[i]);
      }
    }
    i++;
  }
  console.log(second);
}
