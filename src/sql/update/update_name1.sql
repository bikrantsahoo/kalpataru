update CRM_CUSTOMER set CUSTOMER_NAME= CONCAT('$first_name','$middle_name','$last_name')
where CUSTOMER_ID= '$customer_id'