import danieldeveloper.campeonatodefutbol.*;
public class Main {
    public static void main(String[] args){
        Jugador j0 = new Jugador("Amanda", "Laura", "15845421 LP", 24);
        Jugador j1 = new Jugador("Daniel", "Laura", "10021571 LP", 25);
        Jugador j2 = new Jugador("Adriana", "Cusicanqui", "13314855 LP", 23);
        Jugador j3 = new Jugador("Luis", "Laura", "1234568 PT", 14);
        Jugador j4 = new Jugador("Carlos", "Laura", "8795453 OR", 23);
        
        Jugador[] js = new Jugador[5];
        
        js[0] = j0;
        js[1] = j1;
        js[2] = j2;
        js[3] = j3;
        js[4] = j4;
        
        Equipo team = new Equipo("FALQUI", "Mixto", js);
        Equipo[] teams = new Equipo[1];
        teams[0] = team;
        
        Campeonato c = new Campeonato("El torneo de la fuerza", teams);
        c.imprimir();
    }
}
