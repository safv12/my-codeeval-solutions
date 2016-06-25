/**
 * CHALLENGE PALINDROME PRIME
 * Write a program which determines the largest prime palindrome less than 1000.
 *
 * INPUT SAMPLE:
 * There is no input for this program.
 *
 * OUTPUT SAMPLE:
 * Print to stdout the largest prime palindrome less than 1000.
 *
 *     929
 */

function isPrimeNumber(number) {
  if (number <= 3) return number >= 2;

  for (var i = 4; i < number; i++ ) {
    if (number % i === 0) return false;
  }

  return true
}


function isPalindrome(number) {
  reverseNumber = parseInt(number.toString().split("").reverse().join(""));
  return reverseNumber === number;
}


function getGreatestPalindrome(top) {
  var greatest = 0;
  var isPrime = false;

  for (var i = 0; i <= top; i++) {
    isPalindromePrime = isPrimeNumber(i) && isPalindrome(i);
    greatest = (isPalindromePrime) ? i : greatest;
  }

  return greatest
}

var palindrome = getGreatestPalindrome(1000);
console.log(palindrome);
