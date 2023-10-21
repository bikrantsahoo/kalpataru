SELECT ooh.ORDER_NUMBER,oom.MILESTONE,oom.ERROR_MESSAGE,oom.MODULE,oom.T2R_ID,oom.CREATED_ON
FROM OM_ORDER_MILESTONES oom, OM_ORDER_HEADER ooh
WHERE oom.CREATED_ON
between to_date('$start_date', 'dd-mm-yyyy')  and to_date('$end_date', 'dd-mm-yyyy')
AND oom.ERROR_MESSAGE IS NOT NULL
AND ooh.ORDER_HEADER_ID=oom.ORDER_HEADER_ID
order by oom.CREATED_ON desc