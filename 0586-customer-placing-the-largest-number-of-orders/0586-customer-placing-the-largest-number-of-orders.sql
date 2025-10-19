
select customer_number from (
select customer_number, count(*) from orders
group by customer_number
having count(*)=
(select max(c) from(
    select customer_number,count(*) c from orders
    group by customer_number) as temp )
    
) as temp2