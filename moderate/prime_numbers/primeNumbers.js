/**
 * PRIME NUMBERS
 *
 * CHALLENGE DESCRIPTION:
 * Print out the prime numbers less than a given number N. For bonus points your
 * solution should run in N*(log(N)) time or better. You may assume that N is
 * always a positive integer.
 *
 * INPUT SAMPLE:
 * Your program should accept as its first argument a path to a filename. Each
 * line in this file is one test case. Each test case will contain an integer
 * n < 4,294,967,295. E.g.
 *
 *   10
 *   20
 *   100
 *
 * OUTPUT SAMPLE:
 * For each line of input, print out the prime numbers less than N, in ascending
 * order, comma delimited. (There should not be any spaces between the comma and
 * numbers) E.g.
 *
 *   2,3,5,7
 *   2,3,5,7,11,13,17,19
 *   2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
 */

var fileSync = require("fs");

fileSync
  .readFileSync(process.argv[2])
  .toString()
  .split('\n')
  .forEach(function (line) {

    if (line != "") solution(parseInt(line));

  });


function solution(testCase) {
  var primes = [];

  for (var i = 1; i <= testCase; i++) {
    if (isPrime(i) && i < testCase) primes.push(i);
  }

  console.log(primes.join(','));
}



function isPrime(number) {
  if (number <= 3) return number >= 2;

  for (var i = 2; i < number; i++) {
    if (number % i === 0) return false;
  }

  return true;
}
