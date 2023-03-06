Test Automation for theScore App
===============

### Requirements 
- Tested on MacOS with `Python 3.11 venv`
- Existing Appium server running on `127.0.0.1:4723`
- Emulator Pixel 6 Pro
- theScore APK at [`theScore/asset/theScore_Apkpure.apk`](https://github.com/Jasmeen6191/theScore/blob/main/assets/theScore_Apkpure.apk)

### Installation instructions
- Install & Activate Python virtual environment
   ````bash
   % pip3 install virtualenv
   % virtualenv -p python3 venv
   % source venv/bin/activate
   (venv) theScore % pip install -r requirements.txt
   ````
   
### Run Instructions
- Update `"appium:udid"` in file `pages/base/LaunchApp.py` from output of your `adb devices` command in terminal
  Eg.
  ```bash
  % adb devices
  List of devices attached
  emulator-5554	device
  ```
- Run main project
   ```bash
   (venv) theScore % python main.py
    #sample output
    Starting theScores testcases automation project
    This run is completed, please find log file and screenshots in reports directory
   ```
   
### Test Scenario
- Open NCAA Football League,
- Verify that league page opens correctly.
- Tap on sub-tab leaders
- Verify that you are at correct page and NCAA Football leaders are displayed correctly
- Verify that back navigation returns you to the previous page
 
### Explain Automation Framework
- `assets` contains apk file used in this test
- There are app `pages` where control elements properties and methods are written for the score app.
- `base` contains launch app and other required classes to simply the framework
(Please note I only specified the controls that I used and try to make the pages app packge independent,
there's only one control `LocatorType: resource-id` with the locatorValue `:com.fivemobile.thescore:id/big_leader_name`
which is package dependent right now)
- `steps` acts and "reusable blocks".
- `reports` contains test report in the form of logs and screenshots (Note: unit-Html reporting or Allure reporting can be implemented on top of this framework.)
- `utilities` contains logger class
- `testcases` contains the actual test file which is test data parametrize.

### Test Run Reports
- [Test run Report in the form of Run logs](https://github.com/Jasmeen6191/theScore/blob/main/reports/logReportnew.log)
- [Test run Screenshots taken after eahc executed test step](https://github.com/Jasmeen6191/theScore/tree/main/reports/screenshots)


