Update crm_user_login set user_login_id='$new_email_id'
where user_login_id='$old_mail_id' and org_customer_id=636 and status= 'ACTIVE'