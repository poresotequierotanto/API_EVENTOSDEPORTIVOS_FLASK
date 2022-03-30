-- import to SQLite by running: sqlite3.exe db.sqlite3 -init sqlite.sql

PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA foreign_keys = ON;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;
BEGIN TRANSACTION;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `empresa` (
`nombre` TEXT NOT NULL,
`ciudad` TEXT NOT NULL,
`mail` TEXT NOT NULL,
`telefono` TEXT NOT NULL
);

CREATE TABLE `evento` (
`mes` TEXT NOT NULL,
`ano` INTEGER NOT NULL,
`instalacion` TEXT NOT NULL,
`empresaId` TEXT NOT NULL,
`actividad` TEXT NOT NULL,
`deporte` TEXT NOT NULL,
FOREIGN KEY (empresaId) REFERENCES empresa (rowid)
);


CREATE TABLE `participan` (

`id_evento` INTEGER NOT NULL,
`id_part` INTEGER NOT NULL,

PRIMARY KEY (id_evento, id_part),
FOREIGN KEY (id_evento) REFERENCES evento (rowid) 
	ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY (id_part) REFERENCES participante (rowid)  
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE `participante` (
`nombre` TEXT NOT NULL,
`localidad` TEXT NOT NULL,
`telefono` TEXT NOT NULL
);

COMMIT;
PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
