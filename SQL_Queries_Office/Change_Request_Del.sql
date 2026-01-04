-- Query of Delete Change Request 
-- When Change Request not approved from Change Request Management

select * from vtexhchangeorderinit where initno = 'CRNo' 

/*
CRNo - Change Request Number
Initno - Change Request Number
Proslno(Projfc) Fetch from above line select *
woslno(wono) Fetch from above line select *
*/

Begin tran
EXEC [PoppyT].[uisp_Up_Changeorderdelete] 'CRNo',Proslno(Projfcd),woslno(wono)
Rollback

-- Video Link: https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/EZx5vkfsIvFEmcH0M72FjyQB5mWal3QitILK7TgsfZzqEw?e=J0otZQ