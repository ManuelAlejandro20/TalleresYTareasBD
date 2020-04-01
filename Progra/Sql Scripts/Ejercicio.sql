use empresa;
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
    
alter table empleado
	add foreign key(nss_superv) references empleado(nss) on delete cascade on update cascade;
    
alter table empleado
	add foreign key(nd) references departamento(num_departamento) on delete cascade on update cascade;

alter table departamento
	add foreign key(nss_jefe) references empleado(nss) on delete cascade on update cascade;

alter table localizacion_departamento
	add foreign key(num_dep) references departamento(num_departamento) on delete cascade on update cascade;
    
alter table proyecto
	add foreign key(num_dep) references departamento(num_departamento) on delete cascade on update cascade;
    
alter table trabaja_en
	add foreign key(nss_trabajador) references empleado(nss) on delete cascade on update cascade;

alter table trabaja_en
	add foreign key(num_proyecto) references proyecto(numero_proyecto) on delete cascade on update cascade;

alter table familiar
	add foreign key(nsse) references empleado(nss) on delete cascade on update cascade;
    
select *
from departamento d2 join empleado e2 on d2.nss_jefe = e2.nss
where e2.salario > (select avg(e1.salario)
					from empleado e1 join trabaja_en t1 on e1.nss = t1.nss_trabajador join proyecto p1 on t1.num_proyecto = p1.numero_proyecto join departamento d1 on p1.num_dep = d1.num_departamento
					where d1.nombre_departamento = "Administracion");

select e3.nombre_principal, d1.nombre_departamento, p.nombre_proyecto, t.horas, d.nombre_departamento, e4.nombre_principal
from empleado e1 join empleado e2 on e1.nss_superv = e2.nss 
	 join empleado e3 on e2.nss_superv = e3.nss 
     join trabaja_en t on e3.nss = t.nss_trabajador 
     join proyecto p on t.num_proyecto = p.numero_proyecto
     join departamento d on p.num_dep = d.num_departamento
     join empleado e4 on d.nss_jefe = e4.nss,
     departamento d1
where e1.nombre_principal = "Alicia" and e1.inicial = "J" and e1.apellido = "Zelaya" and d1.num_departamento = e3.nd and t.horas > 10;



update empleado e
set e.salario = 43000
where e.nombre_principal = 'Jeniffer' and e.apellido = 'Wallace'