CREATE SCHEMA IF NOT EXISTS sch_tickets;

CREATE TABLE IF NOT EXISTS sch_tickets.airports(
	airport_id SERIAL PRIMARY KEY,
	airport_name VARCHAR(64) UNIQUE,
	airport_city VARCHAR(64) NOT NULL
);

INSERT INTO sch_tickets.airports (airport_name, airport_city)
VALUES
	('Aeroporto Internacional de Guarulhos', 'Guarulhos'),
	('International Airport John F. Kennedy', 'New York'),
	('Aeroporto Deputado Freitas Nobre', 'Cogonhas'),
	('Amsterdam Airport', 'Amsterdam'),
	('Paris Charles de Gaulle', 'Paris')
	('Aeroporto Afonso Pena', 'Curitiba');
	
CREATE TABLE IF NOT EXISTS sch_tickets.flights(
	flight_id SERIAL PRIMARY KEY,
	origin_airport VARCHAR(64) NOT NULL,
	dest_airport VARCHAR(64) NOT NULL,
	flight_date TIMESTAMP NOT NULL,
	price NUMERIC(6,2) NOT NULL,
	capacity SMALLINT NOT NULL,
	passengers SMALLINT NOT NULL,
	CONSTRAINT FK_origin_ap FOREIGN KEY(origin_airport) REFERENCES sch_tickets.airports(airport_name),
	CONSTRAINT FK_destination_ap FOREIGN KEY(dest_airport) REFERENCES sch_tickets.airports(airport_name)
);


INSERT INTO sch_tickets.flights (origin_airport, dest_airport, flight_date, price, capacity, passengers)
VALUES
	('Aeroporto Internacional de Guarulhos', 'Amsterdam Airport', '2021-09-25 11:30:00', 256.50, 128, 0),
	('Amsterdam Airport', 'Paris Charles de Gaulle', '2021-09-27 00:30:00', 480.75, 225, 0),
	('Amsterdam Airport', 'International Airport John F. Kennedy', '2021-09-25 04:45:00', 600.00, 250, 0),
	('Aeroporto Deputado Freitas Nobre', 'Aeroporto Afonso Pena', '2021-09-27 7:00:00', 180.25, 100, 0),
	('Aeroporto Internacional de Guarulhos', 'International Airport John F. Kennedy', '2021-09-25 19:40:00', 990, 300, 0),
	('Aeroporto Internacional de Guarulhos', 'Paris Charles de Gaulle', '2021-09-27 21:00:00', 1280.0, 127, 0),
	('Aeroporto Afonso Pena', 'Aeroporto Deputado Freitas Nobre', '2021-09-27 12:00:00', 300, 200, 0);


CREATE TABLE IF NOT EXISTS sch_tickets.passengers_logins(
	passenger_id SERIAL PRIMARY KEY,
	passenger_name VARCHAR(128) NOT NULL,
	email VARCHAR(128) NOT NULL,
	"password" VARCHAR(64) NOT NULL
);


INSERT INTO sch_tickets.passengers_logins (passenger_name, email, "password")
VALUES ('Lucas Martins', 'lucas@email.com.br', 'Senha123');


CREATE TABLE IF NOT EXISTS sch_tickets.reservations(
	reservation_id SERIAL PRIMARY KEY,
	e_ticket VARCHAR(32) UNIQUE NOT NULL,
	passenger_id INT NOT NULL,
	flight_id INT NOT NULL,
	CONSTRAINT FK_passenger_id FOREIGN KEY(passenger_id) REFERENCES sch_tickets.passengers_logins(passenger_id),
	CONSTRAINT FK_flight_id FOREIGN KEY(flight_id) REFERENCES sch_tickets.flights(flight_id)
);
