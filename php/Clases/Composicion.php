<?php

class Composicion {

    private $nombre;
	private $descripcion;
	private $idTipoComposicion;
	private $idComposicion;
    
    public function __construct($nombre = null, $descripcion = null, $idTipoComposicion = null, $idComposicion = null) {
        $this->idComposicion = $idComposicion;
        $this->nombre = $nombre;
        $this->idTipoComposicion = $idTipoComposicion;
        $this->descripcion = $descripcion;
	}
	
    public function __set($variable, $value) { $this->$variable = $value; }
	public function __get($variable) { return $this->$variable; }
    
    public function creaComposicion() {
		if(!$this->existeComposicion($this->nombre)) {
            $sentencia = Conn()->prepare("INSERT INTO composicion VALUES (null, :nombre, :descripcion, :idTipoComposicion)");
            $sentencia->bindParam(":nombre", $this->nombre);
            $sentencia->bindParam(":descripcion", $this->descripcion);
            $sentencia->bindParam(":idTipoComposicion", $this->idTipoComposicion);
            $sentencia->execute();
            return $sentencia->rowCount() >= 1;
        }
        else { 
            print 'YA EXISTE UN PLATO CON NOMBRE: ' .$this->nombre;
            return false; }
	}
	
	public static function borraComposicion($idComposicion) {
		$sentencia = Conn()->prepare("DELETE FROM composicion WHERE IdComposicion = :idComposicion");
		$sentencia->bindParam(":idComposicion", $idComposicion);
		$sentencia->execute();
		return $sentencia->rowCount() >= 1;
	}
    
    public static function existeComposicion($nombreComposicion) {
        $nombreComposicion = "%".$nombreComposicion."%";
        $consulta = "SELECT COUNT(*) AS Total
                        FROM composicion c
                        WHERE LOWER(c.Nombre) LIKE LOWER(:nombreComposicion)";
        $sentencia = Conn()->prepare($consulta);
        $sentencia->bindParam(":nombreComposicion", $nombreComposicion);
        $sentencia->execute();
        return $sentencia->fetch()['Total'] >= 1;
    }

    public static function CargaTiposComposicion() {
        return Conn()->query("SELECT IdDetalleComposicion, Descripcion FROM detallecomposicion")->fetchAll();
    }

    public static function CargaTodosComposicion() {
        return Conn()->query("SELECT c.IdComposicion, c.Nombre, dc.Precio, dc.Descripcion Tipo FROM composicion c JOIN detallecomposicion dc USING (IdDetalleComposicion)")->fetchAll();
    }

    public static function CargaComposicion($idComposicion) {
        $consulta = "SELECT IdComposicion, Nombre, IdDetalleComposicion FROM composicion JOIN detallecomposicion USING(IdDetalleComposicion) WHERE IdComposicion = :idComposicion";
        $sentencia = Conn()->prepare($consulta);
        $sentencia->bindParam(":idComposicion", $idComposicion);
        $sentencia->execute();
        return $sentencia->fetch();
    }
}