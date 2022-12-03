//import isodd from "is-odd";
const isodd = require("is-odd");
const informacion= require("./info-adicional");

const esPar = isodd(15)

console.log("hola");
console.log(esPar);

//ahora utilizamos lo que hemos exportado desde el otro
//archivo
console.log(informacion.edad);
const saludo = informacion.saludar("Rigoberto");
console.log(saludo);