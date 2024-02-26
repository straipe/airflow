from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import regist, regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 2, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    regist_t2 = PythonOperator(
        task_id="regist_t2",
        python_callable=regist2,
        op_args=["straipe", "man", "kr", "seoul"],
        op_kwargs={"email": "straipe@naver.com", "phone": "010-6779-6060"},
    )
