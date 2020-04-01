create or replace trigger salario_t
before insert on empleado
for each row
begin 
    if (:new.salario > 100000) then
        raise_application_error(-20001, 'Error: salario no puede exceder los $100000, Dato ingresado: $' || :new.salario);
    end if;
end;    
        
insert into empleado(nombre, inic, apellido, nss, fecha_ncto, direccion, sexo, salario, nss_superv, nd) values 
        ('Manuel', 'A', 'Trigo', 199678760, to_date('1998-09-18','yyyy-mm-dd'), 'Palestina 1315, Antofagasta, Chile', 'H', 20000, 333445555, 5);
        
delete from empleado
where nss = 199678760;

declare 
    nombrec cambio.nombre%type;
    inicc cambio.inic%type;
    apellidoc cambio.apellido%type;
    nssc cambio.nss%type;
    fecha_nctoc cambio.fecha_ncto%type;
    direccionc cambio.direccion%type;
    sexoc cambio.sexo%type;
    salarioc cambio.salario%type;
    nss_supervc cambio.nss_superv%type;
    ndc cambio.nd%type;
    codigo cambio.codigo%type;
    cursor cambio is select c.nombre, c.inic, c.apellido, c.nss, c.fecha_ncto, c.direccion, c.sexo, c.salario, c.nss_superv, c.nd, c.codigo 
                     into nombrec, inicc, apellidoc, nssc, fecha_nctoc, direccionc, sexoc, salarioc, nss_supervc, ndc, codigo
                     from cambio c;
    
procedure insertar (nombrec2 in cambio.nombre%type, inicc2 in cambio.inic%type, apellidoc2 in cambio.apellido%type,
                      nssc2 in cambio.nss%type, fecha_nctoc2 in cambio.fecha_ncto%type, direccionc2 in cambio.direccion%type,
                        sexoc2 in cambio.sexo%type, salarioc2 in cambio.salario%type, nss_supervc2 in cambio.nss_superv%type, ndc2 in cambio.nd%type) 
is
    nss empleado.nss%type;
    cursor emp is select e.nss into nss from empleado e where e.nss = nssc2;
    begin 
        open emp;
        loop
            fetch emp into nss;
            if (emp%found) then
                dbms_output.put_line('Error: El empleado ya existe');
                exit;
            else
                insert into empleado(nombre, inic, apellido, nss, fecha_ncto, direccion, sexo, salario, nss_superv, nd)values 
                (nombrec2, inicc2, apellidoc2, nssc2, fecha_nctoc2, direccionc2, sexoc2, salarioc2, nss_supervc2, ndc2);
                exit;
            end if;
        end loop;
        close emp;
    end insertar;
begin 
    open cambio;
    loop 
        fetch cambio into nombrec, inicc, apellidoc, nssc, fecha_nctoc, direccionc, sexoc, salarioc, nss_supervc, ndc, codigo;
        exit when cambio%notfound;
        if(cambio = 'I') then
            insertar(nombrec, inicc, apellidoc, nssc, fecha_nctoc, direccionc, sexoc, salarioc, nss_supervc, ndc);
        elsif(cambio = 'A') then
            null;
        elsif(cambio = 'E') then
            null;
        else
            dbms_output.put_line('Error: El codigo no es valido');
        end if;
    end loop;
    close cambio;
end;