# Python Test Automation Framework

In this project we have automated login test cases for  www.saucedemo.com using python libraries like selenium, pytest
webdriver-manager, pytest-html, pytest-parallel, pytest-xdist

**Pre Requisites**
- Python should be installed on your os (win/linux)
- I have used Python Version 3.7.6
- Headless or Desktop browser (Chrome + FireFox)


**Dependencies Installation**
- In this project we have used 6 different python packages in <py_auto/dependencies/requirements.sh>
- You can install them by executing shell script <requirements.sh> on linux or windows

**Test Case Execution**
- After dependencies installation, your can execute test cases but hitting RUN.sh file(in root directory)
- You can also execute your test cases on demand by passing parameter next to RUN.sh file
  - RUN.sh => will execute all test cases
  - RUN.sh login => will only execute login marked test cases
  - RUN.sh high_priority => will only execute high_priority marked test cases
  - You can find markers dictionary setup.cfg file