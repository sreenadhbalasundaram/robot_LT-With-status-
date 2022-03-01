# bs-robot-framework

## Setup
* Clone the repo
* Install dependencies  `pip install robotframework`  &&  `pip install --upgrade robotframework-seleniumlibrary`
* `pip install robotframework-pabot` -> This is for parallelization 
* For Appium, `pip install robotframework-appiumlibrary` .For more information refer https://github.com/serhatbolsu/robotframework-appiumlibrary
* **Note: This is w.r.t Python3**

## Set lambdatest Credentials 
* You can export the environment variables for the Username and Access Key of your lambdatest account. 

  ```
  export lambdatest_USERNAME=<lambdatest-username> &&
  export lambdatest_ACCESS_KEY=<lambdatest-access-key>
  ```

## Running tests

### Automate
* Navigate to `cd app/test`
* To run single test, run `robot SingleTest.robot`
* To run parallel tests, navigate to 'parallel' folder, run `cd parallel`
  1. Test Suite level
    - Run `pabot --processes <count_of_parallels> *.robot`
    - Alternate method: `pabot --processes <count_of_parallels> <name_of_suites_to_run>` Eg: `pabot --processes 2 Suite1_App.robot       Suite2_App.robot`
  2. Test case level
    - Run `pabot --testlevelsplit <file_name>` Eg:  `pabot --testlevelsplit Suite1.robot`
  3. Run Test cases and Test suites together in parallel
    - Run `pabot --testlevelsplit --processes <count_of_parallels> *.robot`
    - **Note: If the process count exceeds the parallel thread limit, it will automatically get queued. No changes required in the scripts.**
    
### App Automate

* Navigate to `cd app/test`
* Upload app:d
* Add "app_url" to the script. Eg: 
- Android
```
Open Application    ${REMOTE_URL}    app=bs://<app_url>    name=single_test    build=RobotFramework    platformName=Android    os_version=7.0    device=Samsung Galaxy S8
```

* To run single test, run `robot Appium_android.robot` OR  run `robot Appium_ios.robot` 
* Parallel Execution: Same process as Automate

  
## Mobile Browsers (Automate)
* Android: Replace `browser` (i.e. &{DC}[browser]) parameter in `Open Browser` to `android`

