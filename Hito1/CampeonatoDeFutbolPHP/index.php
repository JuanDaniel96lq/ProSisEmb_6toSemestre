<?php
	include "../Campeonato.php";
	$j0 = new Jugador("Amanda", "Laura", "15845421 LP", 24);
	$j1 = new Jugador("Daniel", "Laura", "10021571 LP", 25);
    $j2 = new Jugador("Adriana", "Cusicanqui", "13314855 LP", 23);
    $j3 = new Jugador("Luis", "Laura", "1234568 PT", 14);
    $j4 = new Jugador("Carlos", "Laura", "8795453 OR", 23);

    $js = new Jugador[5];

    $js[0] = $j0;
    $js[1] = $j1;
    $js[2] = $j2;
    $js[3] = $j3;
    $js[4] = $j4;

    $team = new Equipo("FALAQUI", "Mixto", $js);
    $teams = new Equipo[1];

    $teams[0] = $team;

    $c = new Campeonato("El torneo de la fuerza", $teams);
    $c->imprimir();
?>