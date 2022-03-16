<?php
include "./Equipo.php";
	class Campeonato
	{
		private $nombreCampeonato = "";
		private $equipos[] = new Equipo;

		function __construct($name, $teams[])
		{
			$this->nombreCampeonato($name);
			$this->equipos($teams);
		}

		function getNombreCampeonato()
		{
			return $nombreCampeonato;
		}

		function setNombreCampeonato($name){
			$this->nombreCampeonato($name);
		}

		function getEquipos()
		{
			return $equipos;
		}

		function setEquipos($teams[] = new Equipo){
			$this->equipos($teams);
		}

		function imprimir(){
			echo $nombreCampeonato . "<br>";

			for ($i = 0; $i < count($equipos); $i++) { 
				$equipos[$i]->imprimir();
			}
		}
	}
?>