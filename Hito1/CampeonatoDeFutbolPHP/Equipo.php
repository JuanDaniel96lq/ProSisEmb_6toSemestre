<?php
include "./Jugador.php";
	class Equipo
	{
		private $nombreEquipo = "";
		private $categoria = "";
		private $jugadores[] = new Jugador;

		function __construct($name, $category, $players[])
		{
			$this->nombreCompleto($name);
			$this->categoria($category);
			$this->jugadores($players);
		}

		function getNombreEquipo()
		{
			return $nombreEquipo;
		}

		function setNombreEquipo($name){
			$this->nombreEquipo($name);
		}

		function getCategoria()
		{
			return $categoria;
		}

		function setCategoria($category){
			$this->categoria($category);
		}

		function getJugadores()
		{
			return $jugadores;
		}

		function setJugadores($players[] = new Jugador){
			$this->jugadores($players);
		}

		function imprimir(){
			echo $nombreEquipo . "<br>";
			echo $categoria . "<br>";

			for ($i = 0; $i < count($jugadores); $i++) { 
				$jugadores[$i]->imprimir();
			}
		}
	}
?>