/*
  Warnings:

  - You are about to drop the column `cantindad` on the `productos` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE `productos` DROP COLUMN `cantindad`,
    ADD COLUMN `cantidad` INTEGER NOT NULL DEFAULT 10;
