update CRM_CUSTOMER_PERSON
set F_NAME = CONCAT('$first_name','$middle_name') , L_NAME='$last_name'
where CUSTOMER_ID='$customer_id'