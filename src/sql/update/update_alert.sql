UPDATE MON_ALERT_DETAILS SET UPDATED_ON = SYSDATE , state = 'Close'
WHERE TITLE = '$alert_name' AND state = 'Open'