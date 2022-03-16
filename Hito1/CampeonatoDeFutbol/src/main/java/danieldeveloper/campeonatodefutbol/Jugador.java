package danieldeveloper.campeonatodefutbol;

public class Jugador {
    private String nombreCompleto;
    private String apellidos;
    private String ci;
    private int edad;
    
    public Jugador(String name, String lastName, String ci, int age){
        this.nombreCompleto = name;
        this.apellidos = lastName;
        this.ci = ci;
        this.edad = age;
    }

    public String getNombreCompleto() { return nombreCompleto;}
    public void setNombreCompleto(String nombreCompleto) {this.nombreCompleto = nombreCompleto;}
    public String getApellidos() { return apellidos; }
    public void setApellidos(String apellidos) { this.apellidos = apellidos; }
    public String getCi() { return ci; }
    public void setCi(String ci) { this.ci = ci; }
    public int getEdad() { return edad; }
    public void setEdad(int edad) { this.edad = edad; }
    
    public void imprimir(){
        System.out.println("  Nombres: \t" + this.nombreCompleto);
        System.out.println("  Apellidos: \t" + this.apellidos);
        System.out.println("  C.I.: \t" + this.ci);
        System.out.println("  Edad: \t" + this.edad);
        System.out.println();
    }
}
