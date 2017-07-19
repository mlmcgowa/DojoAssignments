function range(start, end, skip){
  var a = start;
  var b = skip;
  var z = end;

  if (z - a === 2){
    return [a + 1];
  }
  else{
    while (a < z) {
      console.log(a);
      a += b;
    }
  }
}
console.log(range(2, 20, 2));
