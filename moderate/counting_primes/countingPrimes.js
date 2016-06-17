/**
 * Given two integers N and M, count the number of prime numbers
 * between N and M (both inclusive)
 *
 * INPUT SAMPLE:
 *
 * Your program should accept as its first argument a path to a
 * filename. Each line in this file contains two comma separated
 * positive integers. E.g.
 *
 * 2,10
 * 20,30
 *
 * OUTPUT SAMPLE:
 *
 * Print out the number of primes between N and M (both inclusive)
 *
 * 4
 * 2
 */

 var fs  = require("fs");


 fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {

   if (line != "") {
     var numbers = line.split(',');

     var totalPrimes = 0;
     for (var i = parseInt(numbers[0]); i <= parseInt(numbers[1]); i++) {
       totalPrimes += (isPrime(i)) ? 1 : 0;
     }

     console.log(totalPrimes);
   }

 });


 function isPrime(number) {
   if (number <= 3) return number >= 2;
   if (number % 2 === 0 || number % 3 === 0) return false;

   for (var i = 4; i < number; i++) {
     if (number % i === 0) return false;
   }

   return true;
 }
