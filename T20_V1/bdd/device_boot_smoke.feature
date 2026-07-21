Feature: Device boot smoke validation

  # This scenario is intentionally small because smoke suites should stay fast and trusted.
  Scenario: Device boots and becomes reachable
    Given a test device with the expected firmware installed
    When the device is powered on
    Then the device should respond to a health check within 30 seconds
    And the main service should report a healthy state