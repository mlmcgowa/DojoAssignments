// var students = [
//      {first_name :  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
// ]
//
// for (var i = 0; i < students.length; i++) {
//  console.log(students[i].first_name, students[i].last_name);
// }

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
 // Students
 // 1 - MICHAEL JORDAN - 13
 // 2 - JOHN ROSALES - 11
 // 3 - MARK GUILLEN - 11
 // 4 - KB TONEL - 7
 // Instructors
 // 1 - MICHAEL CHOI - 11
 // 2 - MARTIN PURYEAR - 13

for (var i = 0; i < users.students.length; i++) {
  console.log("Students");
  console.log(i, "-", users[i].first_name, users[i].last_name, "-");
}
