declare
    nuevonumero accion.numero%type; 
    nuevosaldo accion.saldo%type;
    codigo accion.codigo%type;
    numero cuenta.numero%type;
    cursor accion is select a.numero, a.nuevosaldo, a.codigo into nuevonumero, nuevosaldo, codigo 
                     from accion a;
    cursor cuenta is select c.numero into numero
                     from cuenta c
                     where c.numero = nuevonumero;
begin
    open accion;
    loop 
        fetch accion into nuevonumero, nuevosaldo, codigo;
        exit when accion%notfound;
        open cuenta;
        loop
            fetch cuenta into numero;
            if (cuenta%found) then
                if (codigo = 'I' or codigo = 'A') then
                    update cuenta c
                    set c.salario = nuevosaldo
                    where c.numero = numero;
                elsif(codigo = 'E')then
                    delete from cuenta
                    where numero = numero;
                else
                    dbms_output.put_line('Codigo no valido! no se hicieron cambios');
                end if;
                exit;
            else
                if (codigo = 'I' or codigo = 'A') then
                    insert into cuenta(numero,saldo)values (nuevonumero, nuevosaldo);
                elsif(codigo = 'E')then
                    dbms_output.put_line('Esta cuenta no existe, no se puede eliminar');
                else
                    dbms_output.put_line('Codigo no valido! no se hicieron cambios');
                end if;
                exit;
            end if;
        end loop;
        close cuenta;
    end loop;
    close accion;
end;

declare 
    rutc cambio.rut%type;
    nombrec cambio.nombre%type;
    salarioc cambio.salario%type;
    direccionc cambio.direccion%type;
    fechacontratacionc cambio.fechacontratacion%type;
    codigo cambio.codigo%type;
    cursor cambio is select c.rut, c.nombre, c.salario,c.direccion,c.fechacontratacion,c.codigo into rutc, nombrec, salarioc, direccionc, fechacontratacionc, codigo
                     from cambio c;
    
    procedure insertar(rutc2 in cambio.rut%type, nombrec2 in cambio.nombre%type, salarioc2 in cambio.salario%type, 
                        direccionc2 in cambio.direccion%type, fechacontratacionc2 in cambio.fechacontratacion%type)
    is
    rut empleado.rut%type;
    cursor emp is select e.rut into rut from empleado e where e.rut = rutc2;
    begin
        open emp;
        loop
            fetch emp into rut;
            if (emp%found) then
                dbms_output.put_line('El empleado ya existe, no se puede volver a insertar!');
                exit;
            else
                insert into empleado(rut, nombre, salario, dirección, fechacontratacion)values 
                (rutc2, nombrec2, salarioc2, direccionc2, fechacontratacionc2);
                exit;
            end if;
        end loop;
        close emp;
    end insertar;
    
    procedure actualizar(rutc2 in cambio.rut%type, salarioc2 in cambio.salario%type)
    is
    rut empleado.rut%type;
    cursor emp is select e.rut into rut from empleado e where e.rut = rutc2;
    begin
        open emp;
        loop
            fetch emp into rut;
            if (emp%found) then
                update empleado e 
                set e.salario = salarioc2
                where e.rut = rut;
                exit;
            else
                dbms_output.put_line('Este empleado no existe, no se puede actualizar!');
                exit;
            end if;
        end loop;
        close emp;
    end actualizar;
    
    procedure eliminar(rutc2 in cambio.rut%type)
    is
    rut empleado.rut%type;
    cursor emp is select e.rut into rut from empleado e where e.rut = rutc2;
    begin
        open emp;
        loop
            fetch emp into rut;
            if (emp%found) then
                delete from empleado e
                where e.rut = rut;
                exit;
            else
                dbms_output.put_line('Este empleado no existe, no se puede eliminar!');
                exit;
            end if;
        end loop;
        close emp;
    end eliminar;
    
begin
    open cambio;
    loop 
        fetch cambio into rutc, nombrec, salarioc, direccionc, fechacontratacionc, codigo;
        exit when cambio%notfound;
        if(codigo = 'I') then
            insertar(rutc, nombrec, salarioc, direccionc, fechacontratacionc);
        elsif(codigo = 'A') then
            actualizar(rutc, salarioc);
        elsif(codigo = 'E') then
            eliminar(rutc);
        else
            dbms_output.put_line('Codigo no valido');    
        end if;
    end loop;
    close cambio;
end;

create or replace trigger salario
before update on empleado
for each row
begin  
    if(extract(year from sysdate)- extract(year from :old.fechaContratacion) < 2) then
        raise_application_error(-20001, 'Error: insuficiencia de antiguedad, Dato ingresado: ' || :old.fechaContratacion);
    end if;
end;
