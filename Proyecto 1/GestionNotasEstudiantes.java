import java.util.ArrayList;
import java.util.Scanner;

public class GestionNotasEstudiantes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Estudiante> estudiantes = new ArrayList<>();

        System.out.print("Ingrese la cantidad de estudiantes: ");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consumir el salto de línea

        // Captura de datos de los estudiantes
        for (int i = 0; i < n; i++) {
            System.out.print("Ingrese el nombre del estudiante " + (i + 1) + ": ");
            String nombre = scanner.nextLine();
            System.out.print("Ingrese la nota definitiva de " + nombre + ": ");
            double nota = scanner.nextDouble();
            scanner.nextLine(); // Consumir el salto de línea

            estudiantes.add(new Estudiante(nombre, nota));
        }

        // Cálculo del promedio
        double sumaNotas = 0;
        for (Estudiante estudiante : estudiantes) {
            sumaNotas += estudiante.getNota();
        }
        double promedio = sumaNotas / n;

        // Mostrar resultados
        System.out.printf("La nota promedio del curso es: %.2f%n", promedio);
        System.out.println("Los estudiantes con notas por encima del promedio fueron:");

        int count = 0;
        for (Estudiante estudiante : estudiantes) {
            if (estudiante.getNota() > promedio) {
                count++;
            }
        }
        System.out.println("Los estudiantes con notas por encima del promedio fueron: " + count);

        for (Estudiante estudiante : estudiantes) {
            if (estudiante.getNota() > promedio) {
                System.out.printf("%s: %.2f%n", estudiante.getNombre(), estudiante.getNota());
            }
        }

        scanner.close();
    }
}

class Estudiante {
    private String nombre;
    private double nota;

    public Estudiante(String nombre, double nota) {
        this.nombre = nombre;
        this.nota = nota;
    }

    public String getNombre() {
        return nombre;
    }

    public double getNota() {
        return nota;
    }
}
