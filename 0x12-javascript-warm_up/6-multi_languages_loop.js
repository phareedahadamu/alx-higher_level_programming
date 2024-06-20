#!/usr/bin/node
/* prints 'C is fun', 'Python is cool', 'JavaScript is amazing'
 * using an array of string and a loop
 * using console.log()
 */
const myVar = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
while (i < myVar.length) {
  console.log(myVar[i]);
  i++;
}
