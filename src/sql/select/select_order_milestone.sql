--SELECT ooh.ORDER_NUMBER,oom.MILESTONE,oom.ERROR_MESSAGE,oom.MODULE,oom.T2R_ID,oom.CREATED_ON
--FROM OM_ORDER_MILESTONES oom, OM_ORDER_HEADER ooh
--WHERE oom.CREATED_ON
--between to_date('$start_date', 'dd-mm-yyyy')  and to_date('$end_date', 'dd-mm-yyyy')
--AND oom.ERROR_MESSAGE IS NOT NULL
--AND ooh.ORDER_HEADER_ID=oom.ORDER_HEADER_ID
--order by oom.CREATED_ON desc
--
SELECT ooh.ORDER_NUMBER,poh.PRODUCT_NAME,cul.USER_LOGIN_ID,
oom.MILESTONE,oom.ERROR_MESSAGE,oom.CREATED_ON
FROM OM_ORDER_MILESTONES oom,OM_ORDER_HEADER ooh, PRODUCT_ORDER_HISTORY poh, CRM_USER_LOGIN cul
WHERE  cul.USER_ID=poh.USER_ID
AND OOH.ORDER_NUMBER=poh.ORDER_NUMBER
AND ooh.ORDER_HEADER_ID=oom.ORDER_HEADER_ID
AND oom.CREATED_ON
between to_date('$start_date 00:00:00', 'yyyy-mm-dd hh24:mi:ss')
and to_date('$end_date 23:59:59', 'yyyy-mm-dd hh24:mi:ss')
AND oom.ERROR_MESSAGE IS NOT NULL
ORDER BY poh.ORDER_DATE DESC