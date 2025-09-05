select * from vtmmhordrprocessupdt where serialno=101000001081
select * from vtmmdordrprocessupdt where serialno=101000001081
select *  FROM [AsterT].[vtamhimpayrequest] where rfslno in (101000001081,101000001081002) or  brfslno in (101000001081,101000001081002)

Begin Tran
update s set actstat=0 from vtmmhordrprocessupdt s where projcode=101000374352 and serialno=101000001081
update s set actstat=0  from vtmmdordrprocessupdt s where serialno=101000001081
Rollback

#Delete when third column record not showing

#Note: formname.Serialnumber using inspect element fetch serial number

--Video Link: https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/ERL3xiZCnR5Fti1PegafYRcB9ssCC9ElKlCGF-eukmFsgQ?e=mbIbi2