*** Settings ***
Library    robot1.MathLibrary    # import the Python keyword library

*** Test Cases ***
Add Two Positive Numbers
    ${result}=    Add    2    3
    Should Be Equal As Numbers    ${result}    5

Add Negative Numbers
    ${result}=    Add    -1    -1
    Should Be Equal As Numbers    ${result}    -2

Divide Normal
    ${result}=    Divide    10    3
    Should Be True    ${result} > 3.333 and ${result} < 3.334

Divide By Zero Raises
    Run Keyword And Expect Error    ValueError: Cannot divide by zero
    ...    Divide    10    0

Check Result Type
    ${result}=    Add    1    2
    Should Be Equal As Numbers    ${result}    3
