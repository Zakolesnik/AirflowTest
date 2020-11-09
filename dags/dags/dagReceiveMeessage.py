import time
from pprint import pprint

from common.ServiceBusHelper  import ReceiveMessages

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dagId = 'receive_messages_from_ServiceBus'

dag = DAG(
    dag_id=dagId,
    default_args=args,
    schedule_interval=None,
    start_date=days_ago(2))

task = PythonOperator(
    task_id='task_receive_messages',
    python_callable=ReceiveMessages,    
    dag=dag)
