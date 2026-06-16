from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator

CSV_PATH = "/opt/airflow/data/orders.csv"


def read_csv():
    with open(CSV_PATH) as f:
        rows = f.readlines()

    return len(rows) - 1


def choose_branch(ti):
    rows_count = ti.xcom_pull(task_ids="read_csv")

    if rows_count > 5:
        return "success_branch"

    return "failure_branch"


with DAG(
    dag_id="marketing_batch_poc",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    default_args={
        "owner": "student",
        "retries": 3,
        "retry_delay": timedelta(minutes=1),
        "email": ["student@example.com"],
        "email_on_failure": True,
        "email_on_retry": True,
    },
) as dag:

    read_task = PythonOperator(
        task_id="read_csv",
        python_callable=read_csv,
    )

    branch_task = BranchPythonOperator(
        task_id="branch",
        python_callable=choose_branch,
    )

    success_branch = EmptyOperator(
        task_id="success_branch"
    )

    failure_branch = EmptyOperator(
        task_id="failure_branch"
    )

    read_task >> branch_task
    branch_task >> [success_branch, failure_branch]