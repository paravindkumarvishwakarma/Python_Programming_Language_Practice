select wovalue,* from vtplhproject where projcode='EP-1265'
select wovalue,* from vmunmbranch where brancode='EP-1265'
select wovalue,* from vtplhworkorder where projrfcd=101000395763




begin tran
UPDATE vtplhproject SET wovalue='68439044.00' where serialno=101000395763
UPDATE vmunmbranch SET wovalue='68439044.00' where serialno=101000395763
select wovalue,* from vtplhproject where projcode='EP-1265'
select wovalue,* from vmunmbranch where brancode='EP-1265'
rollback

--Video Ref: https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/EVDCFcX9X7RNq4BmzlSIissB8OEVOopmgCpN9Z2IY3pwgQ?e=jLpS1c