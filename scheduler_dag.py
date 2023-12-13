from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG



with DAG(
    "StockPriceUpdate",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        # "email_on_failure": False,
        # "email_on_retry": False,
        # "retries": 1,
        # "retry_delay": timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function, # or list of functions
        # 'on_success_callback': some_other_function, # or list of functions
        # 'on_retry_callback': another_function, # or list of functions
        # 'sla_miss_callback': yet_another_function, # or list of functions
        # 'trigger_rule': 'all_success'
    },
    description="A simple tutorial DAG",
    schedule_interval='@hourly',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:


    # leduvelStockPriceUpdate_task = PythonOperator(

    #     task_id='leduvelStockPriceUpdate',

    #     python_callable=leduvelStockPriceUpdate,

    #     dag=dag

    # )



    leduvelStockPriceUpdate = BashOperator(
    task_id='leduvelStockPriceUpdate',
    bash_command='python /opt/airflow/dags/main.py --leduvelStockPriceUpdate',
    dag=dag)

    freeformStockPriceUpdate = BashOperator(
    task_id='freeformStockPriceUpdate',
    bash_command='python /opt/airflow/dags/main.py --freeformStockPriceUpdate',
    dag=dag)

    marboStockPriceUpdate = BashOperator(
    task_id='marboStockPriceUpdate',
    bash_command='python /opt/airflow/dags/main.py --marboStockPriceUpdate',
    dag=dag)


    victorinoxStockPriceUpdate = BashOperator(
    task_id='victorinoxStockPriceUpdate',
    bash_command='python /opt/airflow/dags/main.py --victorinoxStockPriceUpdate',
    dag=dag)


    prostoreStockPriceUpdate = BashOperator(
    task_id='prostoreStockPriceUpdate',
    bash_command='python /opt/airflow/dags/main.py --prostoreStockPriceUpdate',
    dag=dag)


# Set the dependencies between the tasks

leduvelStockPriceUpdate >> freeformStockPriceUpdate >> marboStockPriceUpdate >> victorinoxStockPriceUpdate >> prostoreStockPriceUpdate 