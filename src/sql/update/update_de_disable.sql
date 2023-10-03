update HCMP_SPARK_JOBS_DETAILS set status = 'I'
WHERE JOB_INSTANCE_ID = '$job_instance_id' and status = 'A'