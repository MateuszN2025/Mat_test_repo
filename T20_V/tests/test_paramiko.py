import pytest

from T20_V.python.v01_e3_paramiko import main

def test_1_para():
    expected_result = "uid=1000(vboxuser1) gid=1000(vboxuser1) groups=1000(vboxuser1),999(docker),1001(vboxusers)"
    assert main() == expected_result