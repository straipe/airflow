from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id="dags_simple_http_operator",
    start_date=pendulum.datetime(2024, 3, 1, tz="Asia/Seoul"),
    schedule=None,
    catchup=False,
) as dag:

    """서울시 체육시설 공공서비스예약 정보"""
    public_reservation_sport = SimpleHttpOperator(
        task_id="public_reservation_sport",
        http_conn_id="openapi.seoul.go.kr",
        endpoint="{{var.value.api_key_openapi_seoul_go_kr}}/json/ListPublicReservationSport/1/5/",
        method="GET",
        headers={
            "Content-Type": "application/json",
            "charset": "utf-8",
            "Accept": "*/*",
        },
    )

    @task(task_id="python_1")
    def python_1(**kwargs):
        ti = kwargs["ti"]
        result = ti.xcom_pull(task_ids="public_reservation_sport")
        import json
        from pprint import pprint

        pprint(json.loads(result))


public_reservation_sport >> python_1()
