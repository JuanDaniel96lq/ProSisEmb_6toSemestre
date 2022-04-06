package danieldeveloper;

class Writer{
    private String name;
    private String email;
    private String gender;
    private String nationality;

    public Writer(String name, String email, String genero, String nacionalidad){
        this.name = name;
        this.email = email;
        this.gender = genero;
        this.nationality = nacionalidad;
    }
    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return the email
     */
    public String getEmail() {
        return email;
    }

    /**
     * @param email the email to set
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * @return the gender
     */
    public String getGender() {
        return gender;
    }

    /**
     * @param gender the gender to set
     */
    public void setGender(String gender) {
        this.gender = gender;
    }

    /**
     * @return the nationality
     */
    public String getNationality() {
        return nationality;
    }

    /**
     * @param nationality the nationality to set
     */
    public void setNationality(String nationality) {
        this.nationality = nationality;
    }
    
    public String write_book(){
        return this.name + " está escribiendo un libro.";
    }
    
    public String write_a_movie(){
        return this.name + " está escribiendo una pelicula.";
    }
    
    public void change_nationality(String nacionalidad){
        this.setNationality(nacionalidad);
    }
    
    public void change_email(String email){
        this.setEmail(email);
    }
}

public class Main {
    public static void main(String[] args) {
        Writer Instance = new Writer("Daniel", "eate.juandaniel.laura.qu@unifranz.edu.bo", "Masculino", "Boliviana");
        System.out.println("========================");
        System.out.println("Nombre: " + Instance.getName());
        System.out.println("Email: " + Instance.getEmail());
        System.out.println("Genero: " + Instance.getGender());
        System.out.println("Nacionalidad: " + Instance.getNationality());
        
        Instance.change_nationality("Peruana");
        Instance.change_email("Jdaniel@gmail.com");
        
        System.out.println("========================");
        System.out.println("Nombre: " + Instance.getName());
        System.out.println("Email: " + Instance.getEmail());
        System.out.println("Genero: " + Instance.getGender());
        System.out.println("Nacionalidad: " + Instance.getNationality());
    }
}
