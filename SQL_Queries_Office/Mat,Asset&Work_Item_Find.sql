

-----for asset and material find using SQL in all project
select * from UlexM.vmunmresource where itemcode = '1030030080001' -- Item Code
select  pl.projcode,c.costcode,c.costname,r.itemcode,r.itemname from vtexhplanvsactual p
join vtplhproject pl on pl.serialno = p.projrfcd
join vtplhcostcode c on c.serialno = p.costcode
join vmunmresource r on r.serialno = p.rescode 
where p.rescode=101000383451

----service work item find using SQL in all project
select * from vmbdmservicesupply where scode = '115010023006' -- Work Item Code
select  pl.projcode,c.costcode,c.costname,r.scode,r.sname from vtexhplanvsactual p
join vtplhproject pl on pl.serialno = p.projrfcd 
join vtplhcostcode c on c.serialno = p.costcode
join vmbdmServicesupply r on r.serialno = p.rescode 
where p.rescode=101000046832

--Video Link: https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/EaP-mNnqzAVImfDMhUASWNIBlzd19Qce51vd7IOEZfl1pA?e=a4wwDz