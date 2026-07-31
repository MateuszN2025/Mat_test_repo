Feature: ATM Cash Withdrawal
  As a bank customer,
  I want to withdraw cash from an ATM,
  So that I don't have to wait in line at the bank.

  Scenario: Successful withdrawal with sufficient funds
    Given the user has a valid debit card
    And their account balance is $500
    When they request to withdraw $100
    Then the ATM should dispense $100
    And their new account balance should be $400
    And their card should be returned