__author__ = 'Alexander'
from paramiko import AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError

import unittest
import ssh
class test_ssh(unittest.TestCase):

    localRaspberryPiIp = '192.168.1.1'
    def test_live_givenRaspberryPi_internal_whenInvalidUsername(self):
        self.assertEquals(-1, ssh.connect(self.localRaspberryPiIp,'blah','raspberry'))

    def test_live_givenRaspberryPi_internal_whenInvalidPassword(self):
        self.assertEquals(-1, ssh.connect(self.localRaspberryPiIp,'pi','blah'))

    def test_live_givenRaspberryPi_internal_whenValidCredentials(self):
        self.assertEquals(200, ssh.connect(self.localRaspberryPiIp,'pi','raspberry'))

    def test_live_givenRaspberryPi_internal_whenDefaultCredentials(self):
        self.assertEquals(-1, ssh.connect(self.localRaspberryPiIp,'pi','raspberry'))

    #Check the router doesn't provide ssh access on port 22
    def test_live_givenSkyRouterInternal_whenDefaulCredential_thenNoSSH_Allowed(self):
        self.assertRaises(NoValidConnectionsError, ssh.connect, '192.168.0.1','sky','admin')

    externalIp = '2.125.178.194'

    def test_live_givenSkyRouterExternal_whenDefaulCredential_thenNoSSH_Allowed(self):
        self.assertRaises(NoValidConnectionsError, ssh.connect, self.externalIp,'sky','admin')


    #Check that the Raspberry Pi cannot be accessed via SSH through the router on port 22
    def test_live_givenRaspberryPi_external_whenValidCredentials(self):
        self.assertRaises(NoValidConnectionsError, ssh.connect, self.externalIp,'pi','raspberry')

if __name__ == '__main__':
    unittest.main()