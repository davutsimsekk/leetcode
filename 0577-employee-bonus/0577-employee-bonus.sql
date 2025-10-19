select name, bonus
from employee e
left join bonus b
on b.empId=e.empId
where b.empId is null or b.bonus<1000 