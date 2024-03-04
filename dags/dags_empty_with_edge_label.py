from airflow import DAG
import pendulum
from airflow.operators.empty import EmptyOperator
from airflow.utils.edgemodifier import Label

with DAG(
    dag_id="dags_empty_with_edge_label",
    start_date=pendulum.datetime(2024, 3, 1, tz="Seoul/Asia"),
    schedule=None,
    catchup=False,
) as dag:
    empty_1 = EmptyOperator(task_id="empty_1")

    empty_2 = EmptyOperator(task_id="empty_2")

    empty_1 >> Label("1과 2사이") >> empty_2

    empty_3 = EmptyOperator(task_id="empty_3")

    empty_4 = EmptyOperator(task_id="empty_4")

    empty_5 = EmptyOperator(task_id="empty_5")

    empty_6 = EmptyOperator(task_id="empty_6")

    (
        empty_2
        >> Label("2과 6,3,4사이")
        >> [empty_5, empty_3, empty_4]
        >> Label("2,3,4와 6 사이")
        >> empty_6
    )
