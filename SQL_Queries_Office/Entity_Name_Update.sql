select hredocno,* from vmunmentity where entycode='SUP2958'---entity code
	;DISABLE TRIGGER ALL ON Ulexm.unmentity
	update vmunmentity set entname='APCO BUILDING SOLUTIONS PVT. LTD.', lentname='APCO BUILDING SOLUTIONS PVT. LTD.' where entycode='SUP2958'
	;ENABLE TRIGGER ALL ON Ulexm.unmentity
	
select * from vmunmentityresource where submcode='SUP2958'
	update vmunmentityresource set subname='APCO BUILDING SOLUTIONS PVT. LTD.', lsubname='APCO BUILDING SOLUTIONS PVT. LTD.' where submcode='SUP2958'
	select * from vmunmentityresource where submcode='SUP2958'
	
select * from vmunmsupplier where serialno in (101000372581)--hredoc from first query replace all place
	;DISABLE TRIGGER ALL ON Ulexm.unmsupplier
	update vmunmsupplier set sname='APCO BUILDING SOLUTIONS PVT. LTD.', lsname='APCO BUILDING SOLUTIONS PVT. LTD.', orginame='APCO BUILDING SOLUTIONS PVT. LTD.' where serialno=101000372581
	;ENABLE TRIGGER ALL ON Ulexm.unmsupplier
	select * from vmunmsupplier where serialno in (101000372581)

	
select * from vmunmsubcontractor where serialno in (101000372581)
	;DISABLE TRIGGER ALL ON Ulexm.unmsubcontractor
	update vmunmsubcontractor set scname='APCO BUILDING SOLUTIONS PVT. LTD.', lscname='APCO BUILDING SOLUTIONS PVT. LTD.', orginame='APCO BUILDING SOLUTIONS PVT. LTD.' where serialno=101000372581
	;ENABLE TRIGGER ALL ON Ulexm.unmsubcontractor
	select * from vmunmsubcontractor where serialno in (101000372581)

	
select * from vmunmotherservice where serialno in (101000372581)
	;DISABLE TRIGGER ALL ON Ulexm.unmotherservice
	update vmunmotherservice set osname='APCO BUILDING SOLUTIONS PVT. LTD.', losname='APCO BUILDING SOLUTIONS PVT. LTD.', orginame='APCO BUILDING SOLUTIONS PVT. LTD.' where serialno=101000372581
	;ENABLE TRIGGER ALL ON Ulexm.unmotherservice
	select * from vmunmotherservice where serialno in (101000372581)


	
select * from vmunmcustomer where serialno in (101000372581)
	;DISABLE TRIGGER ALL ON Ulexm.unmcustomer
	update vmunmcustomer set cusname='APCO BUILDING SOLUTIONS PVT. LTD.', lcusname='APCO BUILDING SOLUTIONS PVT. LTD.', orginame='APCO BUILDING SOLUTIONS PVT. LTD.' where serialno=101000372581
	;ENABLE TRIGGER ALL ON Ulexm.unmcustomer
	select * from vmunmcustomer where serialno in (101000372581)

	
select * from vmunmprw where serialno in (101000372581)
	;DISABLE TRIGGER ALL ON Ulexm.unmprw
	update vmunmprw set prwname='APCO BUILDING SOLUTIONS PVT. LTD.', lprwname='APCO BUILDING SOLUTIONS PVT. LTD.', orginame='APCO BUILDING SOLUTIONS PVT. LTD.' where serialno=101000372581
	;ENABLE TRIGGER ALL ON Ulexm.unmprw
	select * from vmunmprw where serialno in (101000372581)

--Final Check
select hredocno,* from vmunmentity where entycode='SUP2958'
select * from vmunmentityresource where submcode='SUP2958'
select * from vmunmsupplier where serialno in (101000372581)
select * from vmunmsubcontractor where serialno in (101000372581)
select * from vmunmotherservice where serialno in (101000372581)
select * from vmunmcustomer where serialno in (101000372581)
select * from vmunmprw where serialno in (101000372581)
