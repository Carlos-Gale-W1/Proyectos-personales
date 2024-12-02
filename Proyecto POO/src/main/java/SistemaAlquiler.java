import java.time.LocalDate;
import java.util.ArrayList;

public class SistemaAlquiler {
    private ArrayList<Habitacion> habitaciones;

    public SistemaAlquiler() {
        habitaciones = new ArrayList<>();
    }

    public void agregarHabitacion(Habitacion habitacion) {
        habitaciones.add(habitacion);
    }

    public Habitacion buscarHabitacionDisponible(String tipo, LocalDate fechaInicio, LocalDate fechaFin) {
        for (Habitacion habitacion : habitaciones) {
            if (habitacion.getTipo().equals(tipo) && habitacion.isDisponibilidad()) {
                // Verificar que la habitación esté disponible en el rango de fechas
                return habitacion;
            }
        }
        return null;
    }

    public String realizarReserva(String cliente, String tipo, LocalDate fechaInicio, LocalDate fechaFin) {
        Habitacion habitacion = buscarHabitacionDisponible(tipo, fechaInicio, fechaFin);
        if (habitacion != null) {
            Reserva reserva = new Reserva(cliente, habitacion, fechaInicio, fechaFin);
            habitacion.setDisponibilidad(false);
            return reserva.generarFactura();
        } else {
            return "No hay habitaciones disponibles de este tipo en las fechas seleccionadas.";
        }
    }

    public ArrayList<Habitacion> getHabitaciones() {
        return habitaciones;
    }
}
