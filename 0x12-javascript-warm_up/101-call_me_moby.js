#!/usr/bin/node
/*
 */
function callMeMoby (n, f) {
  let i = 0;
  while (i < n) {
    f();
    i++;
  }
}
module.exports = {
  callMeMoby
};
