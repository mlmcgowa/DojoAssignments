var Arr = [1, "apple", -3, "orange", 0.5];
var numbersOnly = []

for (var i = 0; i < Arr.length; i++) {
  console.log(Arr[i]);
  if (typeof Arr[i] === "number"){
    numbersOnly.push(Arr[i]);
  }
}
console.log(numbersOnly);
