select nss, nombre_principal
from empleado
where nss_superv is null;

select nss, nombre_principal, apellido
from empleado
where salario = (select max(salario) from empleado);

select nombre_principal, upper(nombre_principal)
from empleado;

select count(distinct nss_trabajador)
from trabaja_en;

select nombre_principal, 
case
	when nd = 1 then 'Direccion'
    when nd = 4 then 'Adminsitracion'
    when nd = 5 then 'Investigacion'
    else 'error'
end as 'xd'
from empleado;

select *
from empleado;

select nombre_principal, fecha_ncto, date_add(fecha_ncto, interval 4 month), timestampdiff(month, fecha_ncto ,current_date())
from empleado;

