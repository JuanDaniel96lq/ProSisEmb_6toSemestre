package danieldeveloper.campeonatodefutbol;

public class Campeonato {
    private String nombreCampeonato;
    private Equipo[] equipos;
    
    public Campeonato(String name, Equipo[] team){
        this.nombreCampeonato = name;
        this.equipos = team;
    }
    
    public String getNombreCampeonato(){ return nombreCampeonato; }
    public void setNombreCampeonato(String nombreCampeonato) { this.nombreCampeonato = nombreCampeonato; }
    public Equipo[] getEquipo() { return equipos; }
    public void setEquipo(Equipo[] equipos){ this.equipos = equipos; }
    
    public void imprimir(){
        System.out.println("CAMPEONATO - " + this.nombreCampeonato);
        System.out.println("--------------------------------------");
        for(int i = 0; i < equipos.length; i++){
            equipos[i].imprimir();
            System.out.println("--------------------------------------");
        }
    }
}
