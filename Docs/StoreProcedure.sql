USE restaurante;
-- Se ua la palabra DELIMITER que sirve para indicar que hasta que no vuelva a encontrar la palabra
-- todo sera parte del comando
DELIMITER //
CREATE PROCEDURE DevolverTodosLosUsuarios()
BEGIN
	SELECT * FROM usuarios;
    -- El procedimiento almacenado (store procedure) sirve para un conjunto de operaciones
    -- INSERT INTO platos (...
END //

DELIMITER ;

-- Ahora un SP con parametros
-- en este caso declaramos un parametro de entrada (IN) y a su vez le ponemos un nombre al delimitador
-- si queremos indicar un parametro de salida (OUT)
DROP PROCEDURE IF EXISTS DevolverUsuariosSegunTipo;
DELIMITER //
CREATE PROCEDURE DevolverUsuariosSegunTipo(IN tipo varchar(40), OUT usuarioID INT)-- In significa dato de entrada, OUT sale nos devuelve el id del user
BEGIN
	-- Funciones de agregacion (count, sum, avg, max, min)
    -- COUNT > contabilice cuantos usuarios hay de ese tipo
	SELECT COUNT(id) INTO usuarioId FROM usuarios WHERE tipo_usuario = tipo;
    --  CUENTAME TODOS LOS ID pero guardame en usuarioId
END //

DELIMITER ;

CALL DevolverTodosLosUsuarios();
CALL DevolverUsuariosSegunTipo('ADMIN', @usuarioId);
SELECT @usuarioId;

CALL DevolverUsuariosSegunTipo('USER', @usuarioUser);
SELECT @usuarioUser;