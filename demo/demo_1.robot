*** Settings ***
Library    ../mykonos/
Library    pabot.PabotLib

*** Variables ***
${activity_apk}                                   com.android.messaging/com.android.messaging.ui.conversationlist.ConversationListActivity
${apk}                                            com.android.messaging
${sender_number}                                  0812345678
${message}                                        helllo
@{emulator}                                       192.168.56.131:5555

*** keywords ***
Open Application
    Open App                                        devices_parallel=${emulator}     package=com.android.gallery3d/com.android.gallery3d.app.GalleryActivity

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
    Close App                                       package=com.android.gallery3d      devices_parallel=${emulator}


*** Test Cases ***
Test Case Input Phone Number on Application Messaging
    Log    ${emulator}
    Open Application
    Close Application
