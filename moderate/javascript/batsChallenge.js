

function getParams(line) {
  var data = line.split(' ');

  return {
    'wireLength': data.splice(0, 1)[0],
    'distance': data.splice(0, 1)[0],
    'bats': data
  };
}


function getAllowedBats(data) {
  var allowedBats = ((data.wireLength - 12) / (data.distance - 1)) - data.bats[0];
  allowedBats = Math.floor(allowedBats);

  return (allowedBats <= 0) ? 0 : allowedBats;
}


function run(line) {
  if (line != "") {
    var data = getParams(line);
    var output = getAllowedBats(data);

    return output;
  }
}



var testCases = [
  ['22 2 2 9 11', 3],
  ['33 5 0', 5],
  ['16 3 2 6 10', 0],
  ['835 125 1 113', 5],
  ['47 5 0', 8]
];

testCases.forEach(function(testCase) {
  var result = run(testCase[0]);
  console.log(result === testCase[1]);
});
