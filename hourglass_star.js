let n2 = 5; 
let string2 = "";

for (let i = 0; i < n2; i++) {

  for (let j = 0; j < i; j++) {
    string2 += " ";
  }

  for (let k = 0; k < (n2 - i) * 2 - 1; k++) {
    string2 += "*";
  }
  string2 += "\n";
}

for (let i = 2; i <= n2; i++) {
 
  for (let j = n2; j > i; j--) {
    string2 += " ";
  }
  
  for (let k = 0; k < i * 2 - 1; k++) {
    string2 += "*";
  }
  string2 += "\n";
}
console.log(string2);