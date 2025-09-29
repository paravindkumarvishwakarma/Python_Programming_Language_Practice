--Order_Bili_Type_Change

select billmdl,hredocno,* from vtmmhpurchase where pono ='EP-1257/LPO/MAT/0051' --Order Number

-- 10 means with receipt & 20 means without receipt

make sure no receipt done for any order or amendmend
--update vtmmhpurchase set billmdl=20, trnusrid=-1276 where hredocno=101000131201

--Video Attachment FYR: https://padamsin-my.sharepoint.com/:v:/g/personal/paravind_padams_in/EccVYN6TUjBImtY83Ck3V1QByVs8_wVXwfnbcgmTN3e2gg?e=fOFjv9