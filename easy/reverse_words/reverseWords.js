/**
 * CHALLENGE REVERSE WORDS
 * Write a program which reverses the words in an input sentence.
 *
 * INPUT SAMPLE:
 * The first argument is a file that contains multiple sentences, one per line.
 * Empty lines are also possible.
 *
 * Hello World
 * Hello CodeEval
 *
 * OUTPUT SAMPLE:
 * Print to stdout each sentence with the reversed words in it, one per line.
 * Empty lines in the input should be ignored. Ensure that there are no trailing
 * empty spaces in each line you print.
 *
 * World Hello
 * CodeEval Hello
 */


 var fs  = require("fs");


 fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function(line) {

   if (line != "") {
     var words = line.split(' ');
     var output = "";

     for (var i = words.length; i >= 0; i--) {
       output += words[i] || "";
       output += (words[i - 1]) ? " " : "";
     }

     console.log(output);
   }

 });
