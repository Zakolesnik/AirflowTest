import unittest
from airflow.models import DagBag
from dags.dags import dagReceiveMeessage
from dags.dags import dagSendMeessage

class TestDags(unittest.TestCase):
   
   def setUp(self):
       self.dagbag = DagBag()

   def test_dags_loaded(self):
       self.CheckDagIsLoadedSuccess(dagReceiveMeessage.dagId)
       self.CheckDagIsLoadedSuccess(dagSendMeessage.dagId)

   def CheckDagIsLoadedSuccess(self, dagId):
       dag = self.dagbag.get_dag(dag_id=dagId)
       self.assertDictEqual(self.dagbag.import_errors, {})
       self.assertIsNotNone(dag)
       self.assertEqual(len(dag.tasks), 1)

if __name__ == '__main__':
    unittest.main()