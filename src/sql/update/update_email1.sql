Update crm_cust_contact set cont_value1='$new_email_id'
where cont_type= 'EMAIL'
and customer_id='$old_mail_id'
--(select customer_id from crm_user_login
--where user_login_id='$old_mail_id' and org_customer_id=636);