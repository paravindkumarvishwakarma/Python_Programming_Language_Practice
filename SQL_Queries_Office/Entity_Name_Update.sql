select hredocno,* from vmunmentity where entycode='SUB1045'---entity code
	--;DISABLE TRIGGER ALL ON Ulexm.unmentity
	--update vmunmentity set entname='DEMO CIVIL - 1', lentname='DEMO CIVIL - 1' where entycode='SUB1045'
	--;ENABLE TRIGGER ALL ON Ulexm.unmentity
	
select * from vmunmentityresource where submcode='SUB1045'
	--update vmunmentityresource set subname='DEMO CIVIL - 1', lsubname='DEMO CIVIL - 1' where submcode='SUB1045'
	
select * from vmunmsupplier where serialno in (101000395402)--hredoc from first query replace all place
	--;DISABLE TRIGGER ALL ON Ulexm.unmsupplier
	--update vmunmsupplier set sname='DEMO CIVIL - 1', lsname='DEMO CIVIL - 1', orginame='DEMO CIVIL - 1' where serialno=101000395402
	--;ENABLE TRIGGER ALL ON Ulexm.unmsupplier

	
select * from vmunmsubcontractor where serialno in (101000395402)
	--;DISABLE TRIGGER ALL ON Ulexm.unmsubcontractor
	--update vmunmsubcontractor set scname='DEMO CIVIL - 1', lscname='DEMO CIVIL - 1', orginame='DEMO CIVIL - 1' where serialno=101000395402
	--;ENABLE TRIGGER ALL ON Ulexm.unmsubcontractor

	
select * from vmunmotherservice where serialno in (101000395402)
	--;DISABLE TRIGGER ALL ON Ulexm.unmotherservice
	--update vmunmotherservice set osname='DEMO CIVIL - 1', losname='DEMO CIVIL - 1', orginame='DEMO CIVIL - 1' where serialno=101000395402
	--;ENABLE TRIGGER ALL ON Ulexm.unmotherservice

	
select * from vmunmcustomer where serialno in (101000395402)
	--;DISABLE TRIGGER ALL ON Ulexm.unmcustomer
	--update vmunmcustomer set cusname='DEMO CIVIL - 1', lcusname='DEMO CIVIL - 1', orginame='DEMO CIVIL - 1' where serialno=101000395402
	--;ENABLE TRIGGER ALL ON Ulexm.unmcustomer

	
select * from vmunmprw where serialno in (101000395402)
	--;DISABLE TRIGGER ALL ON Ulexm.unmprw
	--update vmunmprw set prwname='DEMO CIVIL - 1', lprwname='DEMO CIVIL - 1', orginame='DEMO CIVIL - 1' where serialno=101000395402
	--;ENABLE TRIGGER ALL ON Ulexm.unmprw

--https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/EZpj3oY6f-NAqq6l1DP3uWABO773iJztnxqL-Wht-wj5iA?e=Tim2NZ