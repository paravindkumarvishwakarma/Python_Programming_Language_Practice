select appstat,* from vtwfhjoinprocess where empcode='PILS8409'
select * from unmemployee where empcode='PILS8409'
begin tran
update vtwfhjoinprocess set empcode ='PIPS1711' where empcode='PILS8409'
update unmemployee set empcode ='PIPS1711' where empcode='PILS8409'
select appstat,* from vtwfhjoinprocess where empcode='PILS8409'
select * from unmemployee where empcode='PILS8409'
rollback