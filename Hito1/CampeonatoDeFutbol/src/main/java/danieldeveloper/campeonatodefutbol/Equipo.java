package danieldeveloper.campeonatodefutbol;

public class Equipo {
    private String nombreEquipo;
    private String categoria;
    private Jugador jugadores[];
    
    public Equipo(String name, String category, Jugador players[]){
        this.nombreEquipo = name;
        this.categoria = category;
        this.jugadores = players;
    }
    
    public String getNombreEquipo() { return nombreEquipo;}
    public void setNombreEquipo(String nombreEquipo) {this.nombreEquipo = nombreEquipo;}
    public String getCategoria() { return categoria; }
    public void setCategoria(String categoria) { this.categoria = categoria; }
    public Jugador[] getJugadores() { return jugadores; }
    public void setJugadores(Jugador jugadores[]) { this.jugadores = jugadores; }
    
    public void imprimir(){
        System.out.println("Equipo: \t" + this.nombreEquipo);
        System.out.println("Categoría: \t" + this.categoria);
        System.out.println("--------------------------------------");
        System.out.println("JUGADORES");
        for(int i = 0; jugadores.length > i; i++){
            jugadores[i].imprimir();
        }
    }
}
