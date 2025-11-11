--Project Work Order Value Update

select wovalue,wrkval,revwrkval,* from vtplhproject where projcode='EP-1231'
select wovalue,* from vmunmbranch where brancode='EP-1231'
select wovalue,* from vtplhworkorder where projrfcd=101000384414

--UPDATE vtplhproject SET wovalue= where serialno=101000384414