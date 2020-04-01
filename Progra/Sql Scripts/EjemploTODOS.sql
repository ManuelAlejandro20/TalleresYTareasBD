create table empleados(
	rut int not NULL,
  	nombre varchar(10) not NULL
);
create table proyecto(
	numProy int not NULL,
  	nombreProy varchar(10) not NULL
);
create table trabaja_en(
	rutEmp int not NULL,
  	numProy INT not NULL,
	horas int not NULL
);
INSERT INTO empleados(rut,nombre)
VALUES
(1,"Manuel"),
(2, "Ana"),
(3, "Naomi"),
(4, "Cosmefulanito"),
(5, "Elver");

INSERT INTO trabaja_en(rutemp,numproy,horas)
VALUES
(1,11,1),

(2,11,5),
(2,12,6),
(2,14,6),
(2,15,6),
(2,16,6),
(2,17,6),

(3,11,7),
(3,12,7),
(3,14,6),
(3,15,6),
(3,16,6),
(3,17,6);

INSERT INTO proyecto(numproy,nombreproy)
VALUES
(11,"PINGAS"),
(12,"HOHOHO"),
(14,"XD"),
(15,"ELJOJOS"),
(16,"XDDDDD"),
(17,"ELKAKAS");

select * 
from empleados e1 
where e1.rut in (
  
select e.rut
from empleados e
where not EXISTS(SELECT *
             FROM proyecto p
             where not EXISTS(SELECT *
                          from trabaja_en t
                          where t.rutEmp = e.rut and t.numProy = p.numProy)))