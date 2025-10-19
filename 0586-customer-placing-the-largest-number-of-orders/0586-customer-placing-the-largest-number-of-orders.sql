
select max(c),customer_number from(
    select customer_number,count(*) c from orders
    group by customer_number) 
    
