delete from person
where exists  (select 1 from(
    select 1
    from person as p2
    where p2.email=person.email
    and person.id>p2.id
) as temp)