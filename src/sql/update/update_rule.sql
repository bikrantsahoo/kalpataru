UPDATE MON_RULE_DEFINATION_MASTER SET STATUS = 'I',UPDATED_ON = SYSDATE
WHERE STATUS = 'A' AND rule_name = '$rule_name'