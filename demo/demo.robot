*** Settings ***
Library    ../mykonos/
*** Variables ***
${emulator}               192.168.56.106:5555
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
