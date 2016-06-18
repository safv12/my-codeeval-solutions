/**
 * MULTIPLES OF A NUMBER
 *
 * Given numbers x and n, where n is a power of 2, print out the smallest
 * multiple of n which is greater than or equal to x. Do not use division
 * or modulo operator.
 *
 * INPUT SAMPLE:
 * The first argument will be a path to a filename containing a comma
 * separated list of two integers, one list per line. E.g.
 *
 *   13,8
 *   17,16
 *
 * OUTPUT SAMPLE:
 * Print to stdout, the smallest multiple of n which is greater than or equal
 * to x, one per line. E.g.
 *
 *   16
 *   32
 */

var fileSync = require('fs');

fileSync
  .readFileSync(process.argv[2])
    .toString()
    .split('\n')
  .forEach(function(line) {
    if (line) solution(line.split(','));
  });


function solution(testCase) {
  var comparison = parseInt(testCase[0]);
  var power = parseInt(testCase[1]);
  var multiple = parseInt(testCase[1]);

  while (comparison > multiple) {
    multiple += power;
  }

  console.log(multiple);
}
