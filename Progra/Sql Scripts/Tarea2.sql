create table empleado(
	rut varchar(60) not null,
    nombre varchar(60) not null,
    apellido varchar(60) not null,
    salario int not null,
	rutJefe varchar(60),
    codDepto int not null,
    
    primary key(rut)
);

create table departamento(
	codDepto int not null,
    nombre varchar(60) not null,
    presupuesto int not null,
	ubicacion varchar(60) not null,
    rutJefeDepto varchar(60) not null,

    primary key(codDepto)
);

create table proyecto(
	codProyecto int not null,
    nombre varchar(60) not null,
    presupuesto int not null,
	codDeptoControla int not null,
    rutJefeProyecto varchar(60) not null,

    primary key(codProyecto)
);

create table trabaja_en(
	rut varchar(60) not null,
    codProyecto int not null,
    cantHoras int not null,
    
    primary key(rut, codProyecto)
);

insert into empleado(rut, nombre, apellido, salario, rutJefe, codDepto)
	values
		('123456789', 'Hola', 'H', 123456, '111111111', 1),
        ('147258369', 'MU', 'M', 222222, '222222222', 2),
        ('987654321', 'Adios', 'A', 654321, '222222222', 3),
        ('111111111', 'Si', 'S', 111111, '123456789', 3),
        ('222222222', 'No', 'N', 2000000, null, 3);

select p.nombre
from proyecto p join empleado e on p.rutJefeProyecto = e.rut
where p.presupuesto > (select sum(e1.salario) 
					   from empleado e1
                       where e1.codDepto = e.codDepto);
                       
select e.nombre, e.apellido, p.nombre, e1.nombre
from  empleado e join trabaja_en t on e.rut =  t.rut 
	  join proyecto p on t.codProyecto = p.codProyecto 
      join departamento d on p.codDeptoControla = d.codDepto
      join empleado e1 on d.rutJefeProyecto = e1.rut
where e.salario > (select e2.salario 
				   from empleado e2 
				   where e2.rut = e.rutJefe) and d.nombre = "Administracion";

select ed.nombre
from (select * from empleados e join departamento d on e.codDepto = d.codDepto where d.nombre = "Administracion") ed
where not exists(select *
				 from proyecto p
                 where not exists (select *
								   from trabaja_en t
                                   where t.rut = ed.rut and t.codProyecto = p.codProyecto));

select ed.nombre
from (select* from empleado e join departamento d on e.codDepto=d.codDepto where d.nombre="Investigacion") ed,
	  (select * 
	   from (select * 
			from (select* 
				  from proyecto p join departamento d1 on p.codDeptoControla = d1.codDepto 
				  where p.nombre = "Reorganizacion") pd join empleado e1 on pd.rutJefeDepto = e1.rut)) epd
where ed.salario> epd.salario;

select e.nombre
from empleado e join departamento d on e.codDepto = d.codDepto
where d.nombre = "Investigacion" and e.salario > (select e1.salario
												  from proyecto p join departamento d1 on p.codDeptoControla = d1.codProyecto 
													   join empleado e1 on d1.rutJefeDepto = e1.rut
												  where p.nombre = "Reorganizacion");
                                                  
select d.nombre, count(e4.nombre) , sum(e4.salario), avg (e4.salario), max (e4.salario), min (e4.salario)
from empleado e1 join empleado e2 on e1.rutJefe = e2.rut join empleado e3 on e2.rutJefe = e3.rut, 
	 departamento d join empleado e4 on d.codDepto = e4.codDepto
where e1.nombre = "James" and e1.apellido = "Borg" and d.codDepto = e3.codDepto;

select count(t.codProyecto), sum(t.cantHoras)
from departamento d join trabaja_en t on d.rutJefeDepto = t.rut
where d.nombre = "Administracion";
                       
select d.nombre,count(*),sum(e4.salario), avg (e4.salario), max (e4.salario), min (e4.salario)
from empleado e4, 
	(select eee.codDepto 
     from(select e2.rutJefe 
		  from empleado e1 join empleado e2 on e1.rutJefe = e2.rut 
          where e1.nombre = "James " and e1.apellido = "Borg") ee join empleado e3 on ee.rutJefe = e3.rut) eee join departamento d on eee.codDepto = d.codDepto
where e4.codDepto = eee.codDepto;	

select count(t.codProyecto), sum(t.cantHoras)
from (select d.rutJefeDepto 
	  from departamento d  
	  where d.nombre = "Administracion") dr join trabaja_en t on dr.rutJefeDepto = t.rut;
      
select *
from empleados e join trabaja_en t on e1.rut = t.rut join proyectos p on t.codProyecto = p.codProyecto
where p = 'Automatizacion' and e.numDep = any(select e1.numDep 
											  from empleados e1 join empleado e2 on e1.rutJefe = e2.rut
                                              where e1.salario < e2.salario)