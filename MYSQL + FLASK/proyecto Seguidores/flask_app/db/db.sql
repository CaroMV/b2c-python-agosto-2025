-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema registro_seguidores_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `registro_seguidores_db` ;

-- -----------------------------------------------------
-- Schema registro_seguidores_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `registro_seguidores_db` DEFAULT CHARACTER SET utf8 ;
USE `registro_seguidores_db` ;

-- -----------------------------------------------------
-- Table `registro_seguidores_db`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `registro_seguidores_db`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `registro_seguidores_db`.`seguidores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `registro_seguidores_db`.`seguidores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `seguidor_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `fk_usuarios_has_usuarios_usuarios1_idx` (`seguidor_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_usuarios_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_usuarios_has_usuarios_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `registro_seguidores_db`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_usuarios_usuarios1`
    FOREIGN KEY (`seguidor_id`)
    REFERENCES `registro_seguidores_db`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
