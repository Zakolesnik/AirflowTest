import json
import unittest

from dags.common import ServiceBusHelper


class TestServiceBus(unittest.TestCase):
        
    def test_send(self):        
        ServiceBusHelper.SendMessage("--1---")        
        self.assertTrue(True)

    def test_receive(self):        
        ServiceBusHelper.ReceiveMessages()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
