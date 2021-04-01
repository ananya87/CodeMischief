let n1 = 5;
let string1 = "";

for (let i = 1; i <= n1; i++) {
  for (let j = 1; j < n1 - i + 1; j++) {
    string1 += " ";
  }
  for (let k = 0; k < 2 * i - 1; k++) {
    string1 += String.fromCharCode(k + 65);
  }
  string1 += "\n";
}

for (let i = 1; i <= n1 - 1; i++) {
  for (let j = 1; j < i + 1; j++) {
    string1 += " ";
  }
  for (let k = 0; k < 2 * (n1 - i) - 1; k++) {
    string1 += String.fromCharCode(k + 65);
  }
  string1 += "\n";
}
console.log(string1);
