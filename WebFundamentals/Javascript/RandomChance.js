// Let's play the slots!
// Make a function that takes a number of quarters (1 quarter = 1 game).
// There is a 1 in 100 chance to win the slot machine (which will give you
// between 50 - 100 quarters -- use Math.random and Math.floor to pick a random
// number of coins).
// While the user still has quarters, use Math.random to determine if they won.
// If they ever win, return the number of quarters (ex: they had 50 remaining
// quarters and won 90, so it should return 140).
// Return 0 if all the quarters were wasted.

// function PlaySlots(numOfQuarters) {
//   while (numOfQuarters > 0) {
//     var win = Math.random();
//     console.log(win);
//
//     if (win < .01) {
//       console.log(numOfQuarters + Math.floor(Math.random()*50)+50);
//     }
//     if (numOfQuarters == 0) {
//       return 0;
//     }
//   }
// }

// function PlaySlots(numOfQuarters) {
//   var win = Math.random();
//   console.log(win);
//
//   for (numOfQuarters > 0; numOfQuarters--;) {
//     if (win < .1) {
//       (Math.floor(Math.random()*50)+50);
//       console.log(numOfQuarters + (Math.floor(Math.random()*50)+50));
//     }
//     if (numOfQuarters == 0){
//       return 0;
//     }
//   }
//   return 0;
// }
// PlaySlots(50);


function PlaySlots(numOfQuarters) {

  while (numOfQuarters > 0) {
    var win = Math.random();
    console.log(win);
    console.log(numOfQuarters--);

    if (numOfQuarters === 0){
      return 0;
    }
    // numOfQuarters = numOfQuarters--;
    if (win < .01) {
      (Math.floor(Math.random()*50)+50);
      console.log(numOfQuarters + Math.floor(Math.random()*50)+50);
      // if (win > .01) {
      //   return 0;

    }
  }
}

PlaySlots(50);
