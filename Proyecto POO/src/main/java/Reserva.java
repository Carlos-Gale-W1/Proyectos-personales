import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Reserva {
    private final String cliente;
    private Habitacion habitacion;
    private LocalDate fechaInicio;
    private LocalDate fechaFin;

    public Reserva(String cliente, Habitacion habitacion, LocalDate fechaInicio, LocalDate fechaFin) {
        this.cliente = cliente;
        this.habitacion = habitacion;
        this.fechaInicio = fechaInicio;
        this.fechaFin = fechaFin;
    }

    public double calcularTotal() {
        long dias = ChronoUnit.DAYS.between(fechaInicio, fechaFin);
        return dias * habitacion.getPrecio();
    }

    public String generarFactura() {
        double total = calcularTotal();
        return "Factura:\nCliente: " + cliente + "\nHabitación: " + habitacion + "\nFecha inicio: " + fechaInicio +
                "\nFecha fin: " + fechaFin + "\nTotal a pagar: " + total;
    }
}
