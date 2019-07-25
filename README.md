![MyKonos](https://user-images.githubusercontent.com/23183123/61592548-c8c66980-abfe-11e9-9763-e180fb12ab40.png)

RobotFramework - Mykonos
==================================================

Introduction
------------
Mykonos is a complete test automation tools for Android Device using Robot Framework and UI Automator (Python), it easy to learn because Mykonos use BDD syntax to write the test cases.

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
    Library    mykonos

    *** Variables ***
    ${emulator}               192.168.56.103:5555
    ${apk}                    com.android.messaging/com.android.messaging.ui.conversationlist.ConversationListActivity
    ${sender_number}          0812345678
    ${message}                helllo

    *** keywords ***
    Scan Device and Open Application Messaging
        [Arguments]                                               ${input_emulator}     ${input_apk}
        Reset App                                                 ${input_emulator}     ${input_apk}
        Open App                                                  ${input_emulator}     ${input_apk}

    Click Plus Icon on the Messaging Menu
        Click Element                                             resourceId=com.android.messaging:id/start_new_conversation_button

    Type Sender Number
        [Arguments]                                               ${input_sender_number}
        Input Text                                                resourceId=com.android.messaging:id/recipient_text_view     input=${input_sender_number}

    Press Enter
        Press Keycode                                             enter

    Input Message on the Text Area
        [Arguments]                                               ${input_message}
        Input Text                                                resourceId=com.android.messaging:id/compose_message_text      input=${input_message}

    Click Button Send
        Click Element                                             resourceId=com.android.messaging:id/self_send_icon

    *** Test Cases ***
    Test Case Input Phone Number on Application Messaging
        Scan Device and Open Application Messaging                ${emulator}       ${apk}
        Click Plus Icon on the Messaging Menu
        Type Sender Number                                        ${sender_number}
        Press Enter
        Input Message on the Text Area                            ${message}
        Click Button Send
        Page Should Contain Text                                  text=${message}
        Quit App                                                  ${emulator}       ${apk}
        Close App

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
