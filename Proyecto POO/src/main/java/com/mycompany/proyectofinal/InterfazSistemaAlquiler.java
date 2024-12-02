package com.mycompany.proyectofinal;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import java.time.LocalDate;

public class InterfazSistemaAlquiler extends Application {
    private SistemaAlquiler sistema;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        sistema = new SistemaAlquiler();

        primaryStage.setTitle("Sistema de Alquiler de Habitaciones");

        TabPane tabPane = new TabPane();

        Tab tabGestionHabitaciones = new Tab("Gestión de Habitaciones");
        tabGestionHabitaciones.setContent(crearTablaHabitaciones());
        tabPane.getTabs().add(tabGestionHabitaciones);

        Tab tabReservas = new Tab("Reservas");
        tabReservas.setContent(crearFormularioReserva());
        tabPane.getTabs().add(tabReservas);

        Scene scene = new Scene(tabPane, 800, 600);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private TableView<Habitacion> crearTablaHabitaciones() {
        TableView<Habitacion> tablaHabitaciones = new TableView<>();
        TableColumn<Habitacion, Integer> colNumero = new TableColumn<>("Número");
        colNumero.setCellValueFactory(new PropertyValueFactory<>("numero"));

        TableColumn<Habitacion, String> colTipo = new TableColumn<>("Tipo");
        colTipo.setCellValueFactory(new PropertyValueFactory<>("tipo"));

        TableColumn<Habitacion, Double> colPrecio = new TableColumn<>("Precio");
        colPrecio.setCellValueFactory(new PropertyValueFactory<>("precio"));

        TableColumn<Habitacion, Boolean> colDisponibilidad = new TableColumn<>("Disponibilidad");
        colDisponibilidad.setCellValueFactory(new PropertyValueFactory<>("disponibilidad"));

        TableColumn<Habitacion, String> colDescripcion = new TableColumn<>("Descripción");
        colDescripcion.setCellValueFactory(new PropertyValueFactory<>("descripcion"));

        tablaHabitaciones.getColumns().addAll(colNumero, colTipo, colPrecio, colDisponibilidad, colDescripcion);

        // Añadir algunas habitaciones de ejemplo
        sistema.agregarHabitacion(new Habitacion(101, "Individual", 50.0, true, "Habitación individual estándar"));
        sistema.agregarHabitacion(new Habitacion(102, "Doble", 80.0, true, "Habitación doble estándar"));
        sistema.agregarHabitacion(new Habitacion(103, "Suite", 150.0, true, "Suite de lujo"));

        tablaHabitaciones.getItems().addAll(sistema.getHabitaciones());

        return tablaHabitaciones;
    }

    private GridPane crearFormularioReserva() {
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);

        Label lblCliente = new Label("Cliente:");
        TextField txtCliente = new TextField();
        grid.add(lblCliente, 0, 0);
        grid.add(txtCliente, 1, 0);

        Label lblTipo = new Label("Tipo de Habitación:");
        TextField txtTipo = new TextField();
        grid.add(lblTipo, 0, 1);
        grid.add(txtTipo, 1, 1);

        Label lblFechaInicio = new Label("Fecha Inicio (YYYY-MM-DD):");
        TextField txtFechaInicio = new TextField();
        grid.add(lblFechaInicio, 0, 2);
        grid.add(txtFechaInicio, 1, 2);

        Label lblFechaFin = new Label("Fecha Fin (YYYY-MM-DD):");
        TextField txtFechaFin = new TextField();
        grid.add(lblFechaFin, 0, 3);
        grid.add(txtFechaFin, 1, 3);

        Button btnReservar = new Button("Reservar");
        grid.add(btnReservar, 1, 4);

        btnReservar.setOnAction(e -> {
            String cliente = txtCliente.getText();
            String tipo = txtTipo.getText();
            LocalDate fechaInicio = LocalDate.parse(txtFechaInicio.getText());
            LocalDate fechaFin = LocalDate.parse(txtFechaFin.getText());
            String factura = sistema.realizarReserva(cliente, tipo, fechaInicio, fechaFin);
            Alert alert = new Alert(Alert.AlertType.INFORMATION, factura);
            alert.showAndWait();
        });

        return grid;
    }
}
