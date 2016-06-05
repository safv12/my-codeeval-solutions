/**
 * CHALLENGE - FIBONACCI SERIES
 *
 * The Fibonacci series is defined as:
 * F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1.
 * Given an integer n >= 0, print out the F(n).
 *
 * INPUT SAMPLE:
 * The first argument will be a path to a filename containing integer numbers,
 * one per line. E.g.
 * 5
 * 12
 *
 * OUTPUT SAMPLE:
 * Print to stdout, the fibonacci number, F(n). E.g.
 * 5
 * 144
 */

var fs  = require("fs");


function getFibonnacciSerie(top) {
  var tmp = 0;
  var backup = 0;
  var current = 1;
  var serie = [0];

  for (var i = 1; i <= top; i++) {
    serie.push(current);
    tmp = current;
    current = current + backup;
    backup = tmp;
  }

  return serie;
}


fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {

  if (line != "") {
    line = parseInt(line);

    var fibonacciSerie = getFibonnacciSerie(line);

    // Print last position
    console.log(fibonacciSerie[fibonacciSerie.length - 1]);
  }

});
