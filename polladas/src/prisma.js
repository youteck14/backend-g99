import prisma from "@prisma/client";
//la conexion a nuestra base de datos
//usando el patron singleton solamente generamos una conexion
//para todo nuestro proyecto
export const Prisma = new prisma.PrismaClient();

