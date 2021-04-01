let q = 6; 
 let strings = "";
 
 for (let i = 1; i <= q; i++) {
 
   for (let j = 1; j <= q - i; j++) {
     strings += " ";
   }
 
   for (let k = 0; k < 2 * i - 1; k++) {
     strings += "*";
   }
   strings += "\n";
 }
 console.log(strings);