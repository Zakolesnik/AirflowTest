import time
import pytz
from pprint import pprint
from datetime import datetime

from common.ServiceBusHelper  import SendMessage

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

dagId = 'send_message_to_ServiceBus'

dag = DAG(
    dag_id=dagId,
    default_args=args,
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['example'])

task = PythonOperator(
    task_id='task_send_message',
    python_callable=SendMessage,
    op_args=['example of message at {0}'.format(str(datetime.now(pytz.timezone('US/Eastern'))))],
    dag=dag)
