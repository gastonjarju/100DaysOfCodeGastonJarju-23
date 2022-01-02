var person = {
  name: "Gaston",
  age : "24",
  address: {
    street: "101 Chestnut Street",
    city: "Berea"
  },
  children: ["Liberty","Ebe"]

  }

  var friends = [
    {
      name: "Liberty",
      hobby: "Music"
    },
    {
      name: "Ebe",
      hobby: "Matching with Wuranyaas"
    }

  ]


person = JSON.stringify(person);
person = JSON.parse(person);

friends = JSON.stringify(friends)
friends = JSON.parse(friends)


console.log(person.address.city);
console.log(friends[0].name)

/* 100DAYS OF CODING CHALLENGE-----
DAY 1:
READ AND LEARNED HOW TO DECLARED VARIABLES.
LEARNED THE DIFFERENT DATA TYPES IN JAVASCRIPT
lEARNED THE DIFFERENT VARIABLE TYPES
CODED AND DEBUGGED USING THE BROWSER CONSOLE AND POP UP WINDOW

*/
// Creating Variables
var firstNumber = "3";
var secondNumber = 5;
var total = Number(firstNumber) + Number(secondNumber) // The Number functions converts other data types to an integer
alert(total);

// Asking for user's input
var firstNumber = prompt("Enter the first number:");
var secondNumber = prompt("Enter the second number:");
var total = Number(firstNumber) + Number(secondNumber); // The Number functions converts other data types to an integer
alert(total);

const codingChallenge = 100;
alert(codingChallenge)

// Writing a function
var personName = prompt("Enter your name:");
function codeSomething (){
  alert (personName + ", welcome to my first javaScript function code");
}


// Writing an if-statement
var userInput = prompt("Enter any number:")
var myNumber = 10;
if(userInput < myNumber){
  alert(userInput + " is less than " + myNumber)
}else{
  alert(userInput + " is greater than " + myNumber)
}
