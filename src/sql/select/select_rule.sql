SELECT mrdrm.rule_id
FROM MON_RULE_DEFINATION_MASTER mrdm,MON_RULE_DEFINATION_RULE_MAPPING mrdrm
WHERE MRDRM.RULEDEFINATION_ID =  MRDM.RULEDEFINATION_ID
AND mrdm.rule_name = '$rule_name'