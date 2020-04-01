create table empleado(
	nombre_principal tinytext not null,
    inicial char(1) not null,
    apellido tinytext not null,
	nss varchar(9) not null,
    fecha_ncto date not null,
    direccion varchar(60) not null,
    sexo char(1) not null,
    salario int not null,
	nss_superv varchar(9),
    nd int not null,
    PRIMARY KEY (nss)
);
    
create table departamento(
	num_departamento int not null,
	nombre_departamento varchar(60) not null,
    fecha_inicio date not null,
    nss_jefe varchar(9) not null,
    PRIMARY KEY (num_departamento, nombre_departamento)
);

create table localizacion_departamento(
	num_dep int not null,
    direccion varchar(60) not null,
    primary key(num_dep, direccion)
);

create table proyecto(
	nombre_proyecto varchar(60) not null,
	numero_proyecto int not null,
    num_dep int not null,
    localizacion varchar(60) not null,
    PRIMARY KEY (numero_proyecto)
);

create table trabaja_en(
	nss_trabajador varchar(9) not null,
	num_proyecto int not null,
    horas float,
    PRIMARY KEY (nss_trabajador, num_proyecto, horas)
);

create table familiar(
	nsse varchar(9) not null,
	nombre_familiar varchar(60) not null,
	sexo_familiar char(1) not null,
    fecha_nac date not null,
    parentesco tinytext not null,
    PRIMARY KEY (nsse, nombre_familiar)
);

insert into departamento(num_departamento, nombre_departamento, fecha_inicio, nss_jefe)
	values 
    (5, 'Investigacion', '1988-05-22' , 333445555),
    (4, 'Administracion', '1995-01-01' , 987654321),
    (1, 'Direccion', '1981-06-19' , 888665555);

insert into empleado(nombre_principal, inicial, apellido, nss, fecha_ncto, direccion, sexo, salario, nss_superv, nd)
	values
    ('John', 'B', 'Smith', 123456789, '1965-01-09', '731 Fondren, Houston, TX', 'H', 30000, 333445555, 5),
    ('Franklin', 'T', 'Wong', 333445555, '1955-12-08', '633 Voss, Houston, TX', 'H', 40000, 888665555, 5),
    ('Alicia', 'J', 'Zelaya', 999887777, '1968-07-19', '3321 Castle, Spring, TX', 'M', 25000, 987654321, 4),
    ('Jeniffer', 'S', 'Wallace', 987654321, '1941-06-20', '291 Berry, Bellaire, TX', 'M', 43000, 888665555, 4),
    ('Rarnesh', 'K', 'Narayan', 666884444, '1962-09-15', '975 Fire Oak, Humble, TX', 'H', 38000, 333445555, 5),
    ('Joyce', 'A', 'English', 453453453, '1972-07-31', '5631 Rice, Houston, TX', 'M', 25000, 333445555, 5),
    ('Ahmad', 'V', 'Jabbar', 987987987, '1969-03-29', '980 Dallas, Houston, TX', 'H', 25000, 987654321, 4),
    ('James', 'E', 'Borg', 888665555, '1937-11-10', '450 Stones, Houston, TX', 'H', 55000, null , 1);
    
insert into localizacion_departamento(num_dep, direccion)
	values
    (1,'Houston'),
    (4,'Stafford'),
    (5,'Bellaire'),
    (5,'Sugarland'),
    (5,'Houston');

insert into proyecto(nombre_proyecto, numero_proyecto, num_dep, localizacion)
	values
	('ProductoX', 1, 5, 'Bellaire'),
    ('ProductoY', 2, 5, 'Sugarland'),
    ('ProductoZ', 3, 5, 'Houston'),
    ('Automatizacion', 10, 4, 'Stafford'),
    ('Reorganizacion', 20, 1, 'Houston'),
    ('Nuevos beneficios', 30, 4, 'Stafford');
    
insert into trabaja_en(nss_trabajador, num_proyecto, horas)
	values 
    ('123456789', 1, 32.5),
    ('123456789', 2, 7.5),
	('666884444', 3, 40.0),
    ('453453453', 1, 20.0),
    ('453453453', 2, 20.0),
    ('333445555', 2, 10.0),
	('333445555', 3, 10.0),
    ('333445555', 10, 10.0),
    ('333445555', 20, 10.0),
    ('999887777', 30, 30.0),
	('999887777', 10, 10.0),
    ('987987987', 10, 35.0),
    ('987987987', 30, 5.0),
    ('987654321', 30, 20.0),
	('987654321', 20, 15.0),
    ('888665555', 20, 0);
    
insert into familiar(nsse, nombre_familiar, sexo_familiar, fecha_nac, parentesco)
	values
    ('333445555', 'Alice', 'M' , '1986-04-05', 'HIJA'),
    ('333445555', 'Theodore', 'H' , '1983-10-25', 'HIJO'),
    ('333445555', 'Joy', 'M' , '1958-05-03', 'ESPOSA'),
    ('987654321', 'Abner', 'H' , '1942-02-26', 'ESPOSA'),
    ('123456789', 'Michael', 'H' , '1088-01-04', 'HIJO'),
    ('123456789', 'Alice', 'M' , '1988-12-30', 'HIJA'),
    ('123456789', 'Elizabeth', 'M' , '1967-05-05', 'ESPOSA');
    
    
select sum(e.salario)
from empleado e 
group by e.nd
having e.nd = 5;

select ifnull(e.nss_superv, "No tiene") as nss_Supervisor
from empleado e 
group by e.nd
having e.nss_superv is null;

select*
from empleado e join departamento d on e.nd = d.num_departamento
     join trabaja_en t on e.nss = t.nss_trabajador
     join proyecto p on t.num_proyecto = p.numero_proyecto
where p.nombre_proyecto="Automatizacion";

insert into trabaja_en(nss_trabajador, num_proyecto, horas)
values
    ('333445555', 1, 10.0),
    ('333445555', 30, 10.0);

select *
from empleado e
where not EXISTS(SELECT *
             FROM proyecto p
             where not EXISTS(SELECT *
                          from trabaja_en t
                          where t.nss_trabajador = e.nss and t.num_proyecto = p.numero_proyecto)) and e.nss in (select f.nsse from familiar f);

select*
from empleado e join departamento d on e.nd = d.num_departamento
     join empleado e1 on e.nss_superv = e1.nss
where e.salario = (select min(salario )from empleado);

select count(*), sum(t.horas), sum(e.salario)
from empleado e join trabaja_en t on e.nss = t.nss_trabajador
	 join proyecto p on t.num_proyecto = p.numero_proyecto
where p.nombre_proyecto = "Reorganizacion"