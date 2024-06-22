#!/usr/bin/node
/*
 */
function addMeMaybe (n, f) {
  n++;
  f(n);
}
module.exports = {
  addMeMaybe
};
