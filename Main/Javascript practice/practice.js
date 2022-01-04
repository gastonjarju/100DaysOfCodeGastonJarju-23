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


/* 100DAYS OF CODING CHALLENGE-----
DAY 2: UNDERSTANDING ARRAYS
READ AND LEARNED HOW TO CREATE ARRAYS.
LEARNED THE DIFFERENT DATA TYPES ARRAYS CAN HOLD IN JAVASRIPT


*/

// The new keyword
var myFriends = new Array (
  "Liberty","Ebenezer","Sliping"

);
console.log(myFriends)
console.log(myFriends[2])


// The Array Literal
var myFriendsCities = ["Harare","Accra","Banjul"];
console.log(myFriendsCities)
console.log(myFriendsCities[2])

var fruits = ['orange','bananas','peas'];
var animals = ['dog', 'cat', 'beer'];
fruitsAndAnimals = fruits.concat(animals);
document.write(fruitsAndAnimals);


/* 100DAYS OF CODING CHALLENGE-----
DAY 3: UNDERSTANDING JQUERY
READ AND LEARNED HOW TO CREATE DOCUMENT READY, JQUERY SYNTA, JQUERY EFFECTS- hide() and show(),
JQUERY EVENT METHODS, JQUERY SELECTORS,



*/
$(document).ready(function(){
  $("button").click(function(){
    $("p").hide();
  });

  $(function(){
    var startDate = $("#startDate");
    startDate.datepicker({
      changeYear: true,
      changeMonth: true,
      minDate:+1,
      dateFormat: "yy-mm-dd",
    }).attr('readonly','readonly');
  });


});
