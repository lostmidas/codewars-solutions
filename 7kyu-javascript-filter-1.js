// While developing a website, you detect that some of the members have troubles logging in.
// Searching through the code you find that all logins ending with a "_" make problems.
// So you want to write a function that takes an array of pairs of login-names and e-mails,
// and outputs an array of all login-name, e-mails-pairs from the login-names that end with "_".

// If you have the input-array:
// [ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
// it should output:
// [ [ "bar_", "bar@bar.com" ] ]

function searchNames(logins){
    return logins.filter(function(value, index) {
        if(value[0].lastIndexOf("_") == value[0].length-1) {
            return true;
        }
        return false;
    });
}
