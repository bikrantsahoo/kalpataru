update HCMP_SPARK_JOBS_DETAILS set status = '$status1'
WHERE JOB_INSTANCE_ID in ($job_instance_id) and status = '$status2'