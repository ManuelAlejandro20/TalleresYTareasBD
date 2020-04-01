set SERVEROUTPUT ON;
declare
    nombre empleado.nombre%type;
    inicial empleado.inic%type;
    apellido empleado.apellido%type;
    found boolean := false;
    cursor emp is select e.nombre,e.inic,e.apellido INTO nombre,inicial,apellido 
                  from empleado e join departamento d on e.nd = d.numerod
                  where d.nombred = 'Investigacion';
begin
    DBMS_OUTPUT.PUT_LINE('1)Nombre de los empleados que trabajan en algún proyecto controlado por el departamento “Investigación”');
    open emp;
    loop
        fetch emp into nombre,inicial,apellido;
        exit when emp%notfound;
        DBMS_OUTPUT.put_line('Nombre: ' || nombre || ' ' || inicial || '. ' || apellido);
        found := true;
    end loop;
    close emp;
    if not found then
        DBMS_OUTPUT.PUT_LINE('No hay registros que coincidan con esta consulta');
    end if; 
end;

declare
    nombre empleado.nombre%type;
    inicial empleado.inic%type;
    apellido empleado.apellido%type;
    fecha_ncto empleado.fecha_ncto%type;
    edad number(2);
    found boolean := false;
    cursor empedad is select e.nombre, e.inic, e.apellido,e.fecha_ncto into nombre,inicial,apellido,fecha_ncto
                      from empleado e join departamento d on e.nd = d.numerod join empleado e1 on e.nss_superv = e1.nss
                      where e.salario < e1.salario and d.nombred = 'Direccion';
begin
    DBMS_OUTPUT.PUT_LINE('3)Nombre y edad de los empleados que trabajan en el departamento “Direccion” y que ganan más que su jefe');
    open empedad;
    loop
        fetch empedad into nombre, inicial, apellido, fecha_ncto;
        exit when empedad%notfound;
        edad := extract(year from sysdate)- extract(year from fecha_ncto);
        DBMS_OUTPUT.PUT_LINE('Nombre: ' || nombre || ' ' || inicial || '. ' || apellido || ' ' || '| Edad:' || ' ' || edad);
        found := true;
    end loop;
    close empedad;
    if not found then
        DBMS_OUTPUT.PUT_LINE('No hay registros que coincidan con esta consulta');
    end if; 
end;

declare
    nombre empleado.nombre%type;
    inicial empleado.inic%type;
    apellido empleado.apellido%type;
    nombred departamento.nombred%type;
    edadminima number(2):= 99;
    edad number(2);
    found boolean := false;
    cursor empjoven is select e.nombre, e.inic, e.apellido,d.nombred into nombre, inicial, apellido, nombred
                       from empleado e join departamento d on e.nd = d.numerod
                       where extract(year from sysdate)- extract(year from e.fecha_ncto) = edadminima;
    cursor edades is (select (extract(year from sysdate)- extract(year from fecha_ncto)) into edad from empleado e1);
begin
    DBMS_OUTPUT.PUT_LINE('5)Datos del empleado más joven de la empresa (el de menor edad): nombre del empleado, nombre del departamento, edad');
    open edades;
    loop 
        fetch edades into edad;
        exit when edades%notfound;
        if edad < edadminima then
            edadminima := edad;
        end if;
    end loop;
    close edades;
    open empjoven;
    loop
        fetch empjoven into nombre, inicial, apellido, nombred;
        exit when empjoven%notfound;
        DBMS_OUTPUT.PUT_LINE('Nombre: ' || nombre || ' ' || inicial || '. ' || apellido || ' ' || '| Nombre del departamento:' || ' ' || nombred);
    end loop;
    close empjoven;
end;

declare
    nombrep proyecto.nombrep%type;
    nombred departamento.nombred%type;
    nombre empleado.nombre%type;
    inicial empleado.inic%type;
    apellido empleado.apellido%type;
    fecha_ncto empleado.fecha_ncto%type;
    direccion empleado.direccion%type;
    found boolean := false;
    cursor datos is select p.nombrep, d.nombred, e.nombre, e.inic, e.apellido, e.fecha_ncto, e.direccion into nombrep, nombred, nombre, inicial, apellido, fecha_ncto, direccion
                    from proyecto p join departamento d on d.numerod = p.nd 
                         join empleado e on d.nss_jefe = e.nss
                    where p.localizacionp = 'Stafford';
begin
    DBMS_OUTPUT.PUT_LINE('7)Para cada proyecto localizado en “Stafford”, indicar el nombre del proyecto, el nombre del departamento que lo controla y el nombre, fecha de nacimiento y dirección del jefe del departamento que controla el proyecto');
    open datos;
    loop 
        fetch datos into nombrep, nombred, nombre, inicial, apellido, fecha_ncto, direccion;
        exit when datos%notfound;
        DBMS_OUTPUT.PUT_LINE('Nombre proyecto: ' || nombrep || ' | Nombre departamento que controla al proyecto: ' || nombred || ' | Nombre jefe del departamento ' || nombre || ' ' || inicial || '. ' || apellido);
        found := true;
    end loop;
    close datos;
    if not found then
        DBMS_OUTPUT.PUT_LINE('No hay registros que coincidan con esta consulta');
    end if; 
end;

declare
    numero empleado.nss%type;
    cursor cuenta is select c.nss into numero
                     from empleado c
                     where c.nss = 333445555;
begin
    open cuenta;
    loop 
        fetch cuenta into numero;
        if cuenta%found then
            dbms_output.put_line(numero);
        ELSE
             EXIT;
        end if;
    end loop;
    close cuenta;
end;

declare
    nss empleadoc.nss%type;
    cursor emp is select e.nss into nss from empleadoc e;
    procedure xd(nssee in empleado.nss%type)
    is
    nsse empleado.nss%type; 
    nombre empleado.nombre%type;
    apellido empleado.apellido%type;
    cursor tr is select e1.nss, e1.nombre, e1.apellido into nsse, nombre, apellido from empleado e1 where e1.nss = nssee;
    begin
        open tr;
        loop
            fetch tr into nsse, nombre, apellido;
            if tr%found then
                dbms_output.put_line(nsse || nombre || apellido);
                exit;
            else
                dbms_output.put_line('NSSE no encontrado:' || nss);
                exit;
            end if;
        end loop;
        close tr;
    end xd;
begin
    open emp;
    loop
        fetch emp into nss;
        exit when emp%notfound;
        xd(nss);
    end loop;
    close emp;
end;

create table empleadoc(
    nss number(9) not null
);

insert into empleadoc(nss) values 
        (123456789);
insert into empleadoc(nss) values 
        (333445555);
insert into empleadoc(nss) values 
        (999887777);
insert into empleadoc(nss) values 
        (222222222);
insert into empleadoc(nss) values 
        (666884444);
insert into empleadoc(nss) values 
        (453453453);
insert into empleadoc(nss) values 
        (111111111);
insert into empleadoc(nss) values 
        (741852963);
insert into empleadoc(nss) values 
        (199678760);
insert into empleadoc(nss) values 
        (888665555);
insert into empleadoc(nss) values 
        (987987987);
insert into empleadoc(nss) values 
        (987654321);