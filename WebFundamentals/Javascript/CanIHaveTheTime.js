var HOUR = 7;
var MINUTE = 15;
var PERIOD = "PM";

if (MINUTE >= 50){
  console.log("It's almost");
  console.log(HOUR + 1);
}
if (MINUTE <= 15){
  console.log("It's just after");
  console.log(HOUR);
}
if (PERIOD == "AM"){
  console.log("in the morning");
}
if (PERIOD == "PM") {
  console.log("in the evening");
}
