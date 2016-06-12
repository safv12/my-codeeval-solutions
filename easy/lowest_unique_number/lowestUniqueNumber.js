/**
 * CHALLENGE LOWEST UNIQUE NUMBER
 * There is a game where each player picks a number from 1 to 9, writes it on
 * a paper and gives to a guide.
 * A player wins if his number is the lowest unique. We may have 10-20 players
 * in our game.
 *
 * INPUT SAMPLE:
 * Your program should accept as its first argument a path to a filename.
 * You're a guide and you're given a set of numbers from players for the round of game.
 * E.g. 2 rounds of the game look this way:
 *
 * 3 3 9 1 6 5 8 1 5 3
 * 9 2 9 9 1 8 8 8 2 1 1
 *
 * OUTPUT SAMPLE:
 * Print a winner's position or 0 in case there is no winner. In the first line of input sample
 * the lowest unique number is 6. So player 5 wins.
 *
 * 5
 * 0
 */

 var fs  = require("fs");


function getElements(line) {
  return line.split(' ');
}


function uniqueElements(elements) {
  var elementsCopy = elements.slice();
  var uniques = [];
  var repeated = [];

  while (elementsCopy.length) {
    var currentElement = elementsCopy.splice(0, 1);

    if (
      elementsCopy.indexOf(currentElement[0]) === -1 &&
      repeated.indexOf(currentElement[0]) === -1
    ) {
      uniques.push(currentElement[0]);
    } else {
      repeated.push(currentElement[0])
    }
  }

  return uniques;
}


function getLowestElement(elements) {
  var currentLowest;

  var lowest = elements.map(function(current) {
    currentLowest = currentLowest || current;
    currentLowest = (current < currentLowest) ? current : currentLowest;
  });

  return currentLowest;
}


fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {

  if (line != "") {
    var elements = getElements(line);
    var uniques = uniqueElements(elements);
    var lowest = getLowestElement(uniques) || 0;
    var winner = elements.indexOf(lowest) + 1;
    console.log(winner);
  }

});
