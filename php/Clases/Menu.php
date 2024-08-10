<?php

class menu {
    
	private $fechaMenu;
	private $composicion;
	
	public function __construct($fechaMenu = null, $composicion = null) {
		$this->fechaMenu = $fechaMenu;
		$this->composicion = $composicion;
	}

    public function __set($variable, $value) { $this->$variable = $value; }
	public function __get($variable) { return $this->$variable; }
	
	public function creaMenu() {
		$countInsert = 0;
		$fecha = is_string($this->fechaMenu) ? $this->fechaMenu : $this->fechaMenu->format('Y-m-d');
		foreach ($this->composicion as $idComposicion) {
			$sentencia = Conn()->prepare("INSERT INTO menu VALUES (null, :fechaMenu, :idComposicion)");
			$sentencia->bindParam(":fechaMenu", $fecha);
			$sentencia->bindParam(":idComposicion", $idComposicion);
			$sentencia->execute();
			
			$countInsert+=$sentencia->rowCount();
		}
	return $countInsert == sizeof($this->composicion);
	}
	
	public function borraMenu($fecha) {
		$fecha = $fecha == null ? date('Y-m-d') : $fecha;
		$sentencia = Conn()->prepare("DELETE FROM menu WHERE DATE(Fecha) = DATE(:fecha)");
		$sentencia->bindParam(":fecha", $fecha);
		$sentencia->execute();
		return $sentencia->rowCount() >= 1;
	}
    
    public static function menuDelDia($fecha = null) {
		$fecha = $fecha == null ? date('Y-m-d') : $fecha;
		$consulta = "SELECT C.IdComposicion, C.Nombre, DC.Precio, DC.Descripcion Tipo
									FROM menu M
									JOIN composicion C USING (IdComposicion)
									JOIN detallecomposicion DC USING (IdDetalleComposicion)
									WHERE DATE(M.Fecha) = DATE(:fecha)
									ORDER BY IdMenu ASC";
        $sentencia = Conn()->prepare($consulta);
        $sentencia->bindParam(":fecha", $fecha);
        $sentencia->execute();
        return $sentencia->fetchAll();
		}

		/*
		public static function CargaMenuHoy() {
			$consulta = "SELECT C.IdComposicion, C.Nombre, DC.Precio, DC.Descripcion Tipo
										FROM menu M
										JOIN composicion C USING (IdComposicion)
										JOIN detallecomposicion DC USING (IdDetalleComposicion)
										WHERE DATE(M.Fecha) = DATE(NOW())
										ORDER BY IdMenu ASC";
			return Conn()->query($consulta)->fetchAll();
		}
		*/
}