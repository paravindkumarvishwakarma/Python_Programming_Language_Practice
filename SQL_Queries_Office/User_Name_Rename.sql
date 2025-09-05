select * from vtwfhresbnk where fstname like '%ADMIN 01%'

begin tran
update vtwfhresbnk set  fstname = 'Lokesh Rana' where serialno = 101000000494
select * from vtwfhresbnk where fstname like '%ADMIN 01%'
rollback
---
select * from vtwfhresbnk where fstname like '%Lokesh%'
-----

select appstat,* from vtwfhjoinprocess where empcode='ADMIN01'
select * from unmemployee where empcode='ADMIN01'

begin tran
update unmemployee set fname ='Lokesh Rana' where empcode='ADMIN01'
select * from unmemployee where empcode='ADMIN01'
rollback

--Video Link: 