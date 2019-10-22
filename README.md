![MyKonos](https://user-images.githubusercontent.com/23183123/61592548-c8c66980-abfe-11e9-9763-e180fb12ab40.png)

RobotFramework - Mykonos
==================================================

Introduction
------------
Mykonos is a complete test automation tools for Android Device using Robot Framework and UI Automator (Python), it easy to learn because Mykonos use BDD syntax to write the test cases.


Prerequisites
-------------
* Download and Install Python3 [Python](https://www.python.org/downloads/)
* Install latest Robot framework latest  base on the guidance [Robotframework](https://github.com/robotframework/robotframework/blob/master/INSTALL.rst)

Installation
------------

     pip install mykonos

Usage
-----
 * Download and Install the android emulator base on the guidance [Genymotion](https://www.genymotion.com/) or [Android Emulator](https://github.com/codepath/android_guides/wiki/Installing-Android-SDK-Tools).
 * Make sure emulator is available by checking with `adb devices`, for more detail info please check the adb command on [ADB Shell](http://adbshell.com/commands/adb-devices) guidance.
 * Make sure Robot Framework is able to run by execute `robot --version` and it will get Robot Framework version as a result.
 * Create a file (sample.robot).
 * Import __Mykonos__ Library on the Robot Framework Test Suite.
 * Write test case base on [Robot Framework](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#libdoc) guidance.

Code Example
-----
Below is the sample test case for testing an Application Messaging (sample.robot).


    *** Settings ***
    Library                                           mykonos

    *** Variables ***
    ${activity_apk}                                   com.android.messaging/com.android.messaging.ui.conversationlist.ConversationListActivity
    ${apk}                                            com.android.messaging
    ${sender_number}                                  0812345678
    ${message}                                        helllo
    ${emulator}                                       192.168.56.131:5555

    *** keywords ***
    Open Application
        Open App                                        devices_parallel=${emulator}     package=${activity_apk}

    Click Icon Message
        Click Element                                   text=Messaging    devices_parallel=${emulator}

    Click Icon New Message
        Click Element                                   resourceId=com.android.messaging:id/start_new_conversation_button   devices_parallel=${emulator}

    Input Phone Number
        [Arguments]                                     ${input_phonenumber}
        Input Text                                      text=To    devices_parallel=${emulator}   input=${input_phonenumber}

    Press Enter
        Press Keycode                                   keys=enter     devices_parallel=${emulator}

    Input Message
        [Arguments]                                     ${input_message}
        Input Text                                      className=android.widget.EditText   devices_parallel=${emulator}   input=${input_message}

    Click Send Message
        Click Element                                   resourceId=com.android.messaging:id/send_message_button    className=android.widget.ImageButton      devices_parallel=${emulator}

    Close Application
        Close App                                       package=${apk}      devices_parallel=${emulator}

    *** Test Cases ***
    Test Case Input Phone Number on Application Messaging
        Open Application
        Click Icon New Message
        Input Phone Number                              ${sender_number}
        Press Enter
        Input Message                                   ${message}
        Click Send Message
        Close Application


Run The Test
------------
Run the test case by execute `robot sample.robot` on your terminal.

Documentation Detail
--------------------
[Mykonos Documentation](https://mykonos.readthedocs.io/)

Contribution
-------------
* Forks repo and clone to your local computer.
* Checkout the source code from development branch.
* Modified, create unit test and make sure the code is running well on local.
* Commit and pull request the changes to development branch.

Contributors
-------------
 * Monica Danesa ([Monica Danesa](https://github.com/monicadanesa)) <br />
 * Ahmad Andriana Khadafi ([Andriana Khadafi](https://github.com/d4f1))
 * Ichsan Hariadi ([Ichsan Hariadi](https://github.com/pythonjokeun))

Credit
-------------
Thanks to [uiautomator](https://github.com/xiaocong/uiautomator)'s and [thewife](https://github.com/pythonjokeun/thewife) author to inspire us to make this library.
