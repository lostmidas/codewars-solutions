// Write a function that takes a single string (word) as argument.
// The function must return an ordered list containing the indexes of all capital letters in the string.

function capitals(word) {
    var ara = [];
    for (var i = 0; i < word.length; i++) {
        if (word[i] == word[i].toUpperCase()) {
            ara.push(i)
        }
    }
    return ara
};
