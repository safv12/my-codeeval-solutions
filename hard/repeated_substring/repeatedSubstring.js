/**
 * You are to find the longest repeated substring in a given text. Repeated
 * substrings may not overlap. If more than one substring is repeated with
 * the same length, print the first one you find.(starting from the beginning
 * of the text).
 *
 * NOTE: The substrings can't be all spaces.
 *
 * INPUT SAMPLE:
 *
 * Your program should accept as its first argument a path to a filename.
 * The input file contains several lines. Each line is one test case. Each
 * line contains a test string. E.g.
 *
 *   banana
 *   am so uniqe
 *
 * OUTPUT SAMPLE:
 *
 * For each set of input produce a single line of output which is the longest
 * repeated substring. If there is none, print out the string NONE. E.g.
 *
 *   an
 *   NONE
 */
 var fs  = require("fs");


 function getSubstrings(text, len) {
   var maxChars = len / 2;
   console.log('banana');

   for (var i = 0; i <= len; i++) {
     var start = 0;
     var end = maxChars;

     // banana
     while (text.substring(start, end)) {
       console.log(start, end);
       console.log(text.substring(start, end));
       start += end;
       end += start;
     }

     maxChars--;
   }
 }


fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {

  if (line != "") {
    // remove spaces
    line = line.replace(/ /g, '');
    // get length
    var len = line.length;
    // get all substrings
    var allSubstrings = getSubstrings(line, len);
    // count repeated
    // get longest
    // print
  }

});
