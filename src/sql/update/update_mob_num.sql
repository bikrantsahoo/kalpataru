UPDATE crm_cust_contact SET UPDATED_ON = SYSDATE ,
CONT_VALUE1 = '$new_mobile_number'
WHERE customer_id = '$customer_id' AND CONT_TYPE = 'MOBILE'