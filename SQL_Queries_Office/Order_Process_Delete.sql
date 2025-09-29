
--Video Link: https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/ERL3xiZCnR5Fti1PegafYRcB9ssCC9ElKlCGF-eukmFsgQ?e=mbIbi2


 select * from vtmmhordrprocessupdt where serialno=101000001413
 select * from vtmmdordrprocessupdt where serialno=101000001413
 select *  FROM [AsterT].[vtamhimpayrequest] where rfslno in (101000001413,101000001413001) or  brfslno in (101000001413,101000001413001)

Begin Tran
update s set actstat=0 from vtmmhordrprocessupdt s where projcode=101000382602 and serialno=101000001413
update s set actstat=0  from vtmmdordrprocessupdt s where serialno=101000001413
Rollback


in  that 3rd query if termamt and balamt getting mismatched den contact dev team

Begin Tran

update s set actstat=0,trnusrid = -1219,trndate = GETDATE() from vtmmhordrprocessupdt s where projcode=101000385788 and serialno=101000001413
update s set actstat=0,trnusrid = -1219,trndate = GETDATE() from vtmmdordrprocessupdt s where serialno=101000001413 
update s set actstat=0,trnusrid = -1219,trndate = GETDATE() from [vtamhimpayrequest] s where serialno=101000010139
Rollback



Order Number: EP-1241/LPO/MAT/0002

Order Process Update: 202 - Deleted
Sernial Number: 101000001413

Order Process Update: 205 - deleted
Serial Number: 101000001413

Order Process Update: 206
Serial Number: 101000001413
