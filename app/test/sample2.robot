*** Settings ***
Library  config2.py
Library  Selenium2Library

*** Variables ***
${remote_url}=    http://:@mobile-hub.lambdatest.com/wd/hub


*** Test Cases ***
Example Test
    ${value}    Capability
    Log         ${value} 
    open browser    remote_url=${remote_url}     desired_capabilities=${value} url=https://www.lambdatest.com/support/docs/appium-python-robot/ 
   
    
   