SELECT *
FROM dojos_ninjas.dojos;

-- -----------------------------------------------------
-- Table `dojos_ninjas`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


INSERT INTO dojos(id, name )
VALUES( 1, 'FightHouse' ),
	  ( 2, 'ChicagoDojo' ),
      ( 3, 'SanJoseDojo' );
      

-- -----------------------------------------------------
-- Table `dojos_ninjas`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

INSERT INTO ninjas(id, first_name, last_name, age, dojo_id )
VALUES( 1, 'Jose', 'Rodriguez', 32, 3 ),
	  ( 2, 'Natalia', 'Castillo', 30, 3 ),
      ( 3, 'Carlos', 'Salas', 25, 2 ),
      ( 4, 'Luis', 'Rojas', 28, 2 ),
      ( 5, 'Raquel', 'Vargas', 25 ,1 ),
      ( 6, 'Mary', 'Miller', 29, 1);
      
SELECT *
FROM dojos_ninjas.ninjas;