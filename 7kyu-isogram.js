// An isogram is a word that has no repeating letters, consecutive or non-consecutive.
// Implement a function that determines whether a string that contains only letters is an isogram.
// Assume the empty string is an isogram. Ignore letter case.

// Examples:
// is_isogram("Dermatoglyphics" ) == true
// is_isogram("aba" ) == false
// is_isogram("moOse" ) == false # -- ignore letter case

function isIsogram(str) {
  str = str.toLowerCase();
  str = str.split("");
  str = str.sort();
  for (var i = 0; i < str.length; i++) {
    if (str[i] === str[i + 1]) {
      return false;
    }
  } return true;
};
