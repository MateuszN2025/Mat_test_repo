"""
Robot Framework - Keyword Library (robot1.py)

In RF architecture:
  .py file   → Keyword Library  (reusable actions written in Python)
  .robot file → Test Suite       (test cases written in RF syntax)

Run the tests with:  robot robot11.robot
"""
from robot.api.deco import keyword, library


# @library turns this class into an RF keyword library
@library(auto_keywords=False)
class MathLibrary:

    # @keyword exposes the method as a usable RF keyword
    @keyword("Add")
    def add(self, a: float, b: float) -> float:
        return float(a) + float(b)

    @keyword("Divide")
    def divide(self, a: float, b: float) -> float:
        a, b = float(a), float(b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
"""
*** Settings ***
Resource  HubjectCommon.robot
->  
*** Settings ***
Resource  robot_suites/common_keywords.robot
->
*** Settings ***
Library  Collections
Library  String
Library  framework_helpers/global_listener.py
Library  python2robot/keywords_common.py
Library  python2robot/keywords_config.py
Library  python2robot/keywords_template.py
Library  python2robot/keywords_threads.py
Library  python2robot/keywords_aws.py
Library  python2robot/keywords_embedded_low_level.py
"""


# robot --pythonpath . robot11.robot

# stop_service  /etc/init.d/S93i2p2app          ← .robot (keyword call)
#   │
#   │  [resolved by Robot via Library declaration in common_keywords.robot]
#   ▼
# def stop_service(service_path, ...)            ← python2robot/keywords_embedded_low_level.py:203
#   │
#   ▼
# service_mgmt_by_name(proc_name, 'stop', ...)   ← utils/helpers/board_services.py
#   │
#   ▼
# send_ssh_command("killall i2p2app", ...)        ← SSH → embedded device