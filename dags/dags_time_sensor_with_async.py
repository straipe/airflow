import pendulum
from airflow import DAG
from airflow.sensors.date_time import DateTimeSensorAsync

with DAG(
    dag_id="dags_time_sensor_with_async",
    start_date=pendulum.datetime(2024, 3, 11, 0, 0, 0),
    end_date=pendulum.datetime(2024, 3, 11, 1, 0, 0),
    schedule="*/10 * * * *",
    catchup=True,
) as dag:
    synce_sensor = DateTimeSensorAsync(
        task_id="sync_sensor",
        target_time="""{{macros.datetime.utcnow() + macro.timedelta(minutes=5) }}""",
    )
