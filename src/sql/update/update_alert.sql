UPDATE MON_ALERT_DETAILS SET UPDATED_ON = SYSDATE , state = 'Close'
WHERE TITLE IN ($alert_name) AND state = 'Open'