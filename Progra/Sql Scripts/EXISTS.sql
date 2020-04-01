select * 
from proyecto p join empleado e on p.rutJefeProyecto = e.rut
where p.presupuesto > (select sum(salario)
						from empleado e1
                        where e1.codDepto = e.codDepto);
                        
select e1.nombre, e1.apellido, p.nombre, e3.nombre
from empleado e1 join empleado e2 on e1.rut = e2.rut 
	 join departamento d on e1.codDepto = d.codDepto 
     join trabaja_en t on e1.rut = t.rut
     join proyecto p on t.codProyecto = p.codProyecto
     join departamento d1 on p.codDeptoControla = d.codDepto
     join empleado e3 on d1.rutJefeDepto = e3.rut
where d.nombre = "Administracion" and e1.salario > e2.salario;

select * 
from empleado e join trabaja_en t on e.nss = t.nss_trabajador join proyecto p on t.num_proyecto = p.numero_proyecto
where p.nombre_proyecto = "Automatizacion";

select distinct e4.nd
from empleado e4
where not exists(select e3.nd
				 from empleado e3
				 where not exists (select e1.nss as eee
								   from empleado e1 join empleado e2 on e1.nss_superv = e2.nss 
								   where e1.salario < e2.salario and e1.nss = e3.nss) and e3.nd = e4.nd);
select distinct e3.nd
from empleado e3
where not exists(
select e1.nd
from empleado e1 join empleado e2 on e1.nss_superv = e2.nss 
where e1.salario > e2.salario and e1.nd = e3.nd ) and e3.nss_superv is not null;



update empleado
set salario = 25000
where nombre_principal = "Alicia"



