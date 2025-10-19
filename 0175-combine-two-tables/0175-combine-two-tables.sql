select p.firstName,p.lastName,ad.city,ad.state 
from Person as p left join Address as ad
on ad.personId = p.personId