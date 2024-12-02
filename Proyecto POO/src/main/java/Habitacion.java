public class Habitacion {
    private int numero;
    private String tipo;
    private double precio;
    private boolean disponibilidad;
    private String descripcion;

    public Habitacion(int numero, String tipo, double precio, boolean disponibilidad, String descripcion) {
        this.numero = numero;
        this.tipo = tipo;
        this.precio = precio;
        this.disponibilidad = disponibilidad;
        this.descripcion = descripcion;
    }

    public int getNumero() {
        return numero;
    }

    public String getTipo() {
        return tipo;
    }

    public double getPrecio() {
        return precio;
    }

    public boolean isDisponibilidad() {
        return disponibilidad;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDisponibilidad(boolean disponibilidad) {
        this.disponibilidad = disponibilidad;
    }

    @Override
    public String toString() {
        return "Habitación " + numero + ": " + tipo + ", Precio: " + precio + ", Disponible: " + disponibilidad;
    }
}
