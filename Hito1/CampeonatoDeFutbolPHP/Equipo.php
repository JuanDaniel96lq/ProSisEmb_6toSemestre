<?php
inlcude "./Jugador.php";
	class Equipo
	{
		private $nombreEquipo = "";
		private $categoria = "";
		private $jugadores[];

		function __construct($name, $lastName, $id, $age)
		{
			$this->nombreCompleto($name);
			$this->apellidos($lastName);
			$this->ci($id);
			$this->edad($age);
		}

		function getNombreCompleto()
		{
			return $nombreCompleto;
		}

		function setNombreCompleto($name){
			$this->nombreCompleto($name);
		}

		function getApellidos()
		{
			return $apellidos;
		}

		function setApellidos($lastName){
			$this->apellidos($lastName);
		}

		function getCi()
		{
			return $ci;
		}

		function setCi($id){
			$this->ci($id);
		}

		function getEdad()
		{
			return $edad;
		}

		function setEdad($age){
			$this->edad($age);
		}

		function imprimir(){
			echo "\t- ". $nombreCompleto;
			echo "\t- ". $apellidos; 
			echo "\t- ". $ci; 
			echo "\t- ". $edad; 
		}
	}
?>