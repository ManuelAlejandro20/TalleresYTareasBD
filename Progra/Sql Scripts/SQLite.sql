select m.a
from r3 m
where not EXISTS(select *
                 from r2 o
                 where not EXISTS(SELECT *
                                  from r1 n
                                  where n.a = m.a and n.b = o.b ))