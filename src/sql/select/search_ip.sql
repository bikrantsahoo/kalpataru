SELECT DISTINCT
rn.IP_ADDRESS ,rn.STATUS  ,rn.RESOURCE_TYPE_ID ,rn.CREATED_ON ,rn.UPDATED_ON ,rn.UPDATED_BY
,ram.NAME ,ram.ASSET_ID ,ram.PROJECT_ID ,ram."SOURCE" , ram.status,ram.ENABLED ,ram.HOSTNAME ,
ram.ORDER_ID ,ram.PROVISIONED_BY ,ram.UPDATED_ON
,hpm.NAME ,hpm.PROJECT_DESC
FROM rm_network_interface rn, rm_asset_master ram, hcmp_project_master hpm
WHERE rn.EXTERNAL_RESOURCE_ID  = ram.EXTERNAL_RESOURCE_ID
AND ram.PROJECT_ID  = hpm.PROJ_ID
AND rn.IP_ADDRESS = '$alert_name'
AND rn.IS_DELETED = 0

--AND ram.STATUS = 'A'

--AND ram.ENABLED = 'Y'