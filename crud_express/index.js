import express, {json} from "express";

const servidor = express()

//use > sirve pra agregar un middleware que validara la informacion dependiendo
//el orden en el que lo coloquemos

//cada vez que llegue infomracion en formaton JSON este middleware lo pueda
//convertir en una informacion legible y la almacene en el req.body
servidor.use(json());
const productos = [
    {
        nombre: "pollada",
        precio: 20.5,
        disponible:true,
    },
    {
        nombre:"adobada",
        precio:15.5,
        disponible:true,
    },
    {
        nombre:"chichorranada",
        precio:17.4,
        disponible:true,
    },
    {
        nombre:"chuleteada",
        precio:12.5,
        disponible:false,
    },
];

servidor.get('/', (req,res)=>{
    console.log("Entro aqui");
    res.status(200).json({
        message:"Bienvenido a mi API de express"
    });
});

servidor
    .route("/productos").get((req,res)=>{
        const result = productos.filter(word => word.disponible ===true);
        res.status(200).json({
            content:result,
        });
    })
    .post((req,res)=>{
        console.log(req.body);
        const data = req.body;

        productos.push(data);//con esto agregamos el nuevo producto

        res.status(201).json({
            content: "Producto creado exitosamente",
        });
    });

servidor.listen(5000, ()=>{
    console.log(`Servidor corriendo exitosamente en el puerto 5000`);
});

