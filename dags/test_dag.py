import duckdb
from airflow.decorators import dag, task 
from pendulum import datetime
from airflow.operators.bash import BashOperator

@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False
)
def test_dag():

    @task
    def duckdb_testing():
        cursor = duckdb.connect()
        print(cursor.execute('SELECT 42').fetchall())

    run_streamlit_test = BashOperator(
        task_id="run_streamlit_test",
        bash_command="streamlit run streamlit_test.py",
        cwd="include"
    )

    duckdb_testing() >> run_streamlit_test

test_dag()