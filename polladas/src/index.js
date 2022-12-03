import express, {json} from "express";

const servidor = express()

//para que cuando me envien BOdy en formato JSON express lo pueda leet y transformar
//a un formato legible
servidor.use(json());
//variable de entorno en formato JSON
//Nullish coalesing operator ?? si null o undefined pasara al
//al otro lado en este caso 5000
const PORT = process.env.PORT ?? 5000;

servidor.listen(PORT,() =>{
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
})