select starttime, endtime, status from hcmp_health_monitor
where job_instance_id = '$job_instance_id' order by starttime desc
fetch first 10 rows only