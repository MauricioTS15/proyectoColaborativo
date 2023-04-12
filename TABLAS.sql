-- MySQL Script generated by MySQL Workbench
-- Wed Apr 12 16:29:38 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Gestión de proyectos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Gestión de proyectos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Gestión de proyectos` DEFAULT CHARACTER SET utf8 ;
USE `Gestión de proyectos` ;

-- -----------------------------------------------------
-- Table `Gestión de proyectos`.`CLIENTE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestión de proyectos`.`CLIENTE` (
  `nombre` VARCHAR(45) NOT NULL,
  `telefono` INT NOT NULL,
  PRIMARY KEY (`nombre`, `telefono`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestión de proyectos`.`PROYECTO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestión de proyectos`.`PROYECTO` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `fecha_inicio` DATE NULL,
  `fecha_fin` DATE NULL,
  `presupuesto` FLOAT NULL,
  `tarea_realizar` VARCHAR(45) NULL,
  `responsable` VARCHAR(45) NULL,
  `CLIENTE_nombre` VARCHAR(45) NOT NULL,
  `CLIENTE_telefono` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_PROYECTO_CLIENTE1_idx` (`CLIENTE_nombre` ASC, `CLIENTE_telefono` ASC) VISIBLE,
  CONSTRAINT `fk_PROYECTO_CLIENTE1`
    FOREIGN KEY (`CLIENTE_nombre` , `CLIENTE_telefono`)
    REFERENCES `Gestión de proyectos`.`CLIENTE` (`nombre` , `telefono`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestión de proyectos`.`EMPLEADO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestión de proyectos`.`EMPLEADO` (
  `id` INT NOT NULL,
  `dni` VARCHAR(9) NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gestión de proyectos`.`TAREA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gestión de proyectos`.`TAREA` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `fecha_inicio` VARCHAR(45) NULL,
  `fecha_fin` VARCHAR(45) NULL,
  `responsable` VARCHAR(45) NULL,
  `nivel_prioridad` INT NULL,
  `estado_tarea` INT NULL,
  `notas_adicionales` VARCHAR(45) NULL,
  `PROYECTO_id` INT NOT NULL,
  `EMPLEADO_id` INT NOT NULL,
  PRIMARY KEY (`id`, `PROYECTO_id`, `EMPLEADO_id`),
  INDEX `fk_TAREA_PROYECTO_idx` (`PROYECTO_id` ASC) VISIBLE,
  INDEX `fk_TAREA_EMPLEADO1_idx` (`EMPLEADO_id` ASC) VISIBLE,
  CONSTRAINT `fk_TAREA_PROYECTO`
    FOREIGN KEY (`PROYECTO_id`)
    REFERENCES `Gestión de proyectos`.`PROYECTO` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TAREA_EMPLEADO1`
    FOREIGN KEY (`EMPLEADO_id`)
    REFERENCES `Gestión de proyectos`.`EMPLEADO` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
