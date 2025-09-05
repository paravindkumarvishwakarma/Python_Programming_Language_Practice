-- Change Delivery Date in Order Entry
select delivdt,hredocno, * from vtmmhpurchase where  pono='EP-1222/WO-BB/0021'
update vtmmhpurchase set delivdt='2025-08-31',trnusrid=-854 where hredocno = 101000061287

--Video Link: 