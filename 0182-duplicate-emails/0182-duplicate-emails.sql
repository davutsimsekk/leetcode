select email
from person as p
group by email
having count(*) > 1