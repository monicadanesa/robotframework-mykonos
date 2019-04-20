*** Settings ***
Library    ../mykonos/

*** Variables ***
${emulator}               emulator-5554
${apk}                    com.android.browser/com.android.browser.BrowserActivity
${element_locator}        android.widget.Button
*** Test Cases ***
Test Open Apps
  ${device}=  Scan Current Device           ${emulator}
  Open Application                          ${emulator}     ${apk}
  ${locator}=  Get locator                  className=android.widget.Button
  Click Element                             className=android.widget.Button
  Close Application                         ${emulator}     ${apk}
