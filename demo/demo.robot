*** Settings ***
Library    ../mykonos/
*** Variables ***
@{emulator}               192.168.56.127:5555   192.168.56.125:5555
${apk}                    com.android.messaging/com.android.messaging.ui.conversationlist.ConversationListActivity
${sender_number}          0812345678
${message}                helllo
${emulator}               192.168.56.127:5555

*** keywords ***
Scan Device and Open Application Messaging
    [Arguments]                                               ${input_emulator}     ${emulator}
    Reset App                                                 ${input_emulator}    ${emulator}
    Open App                                                  ${input_emulator}     ${emulator}

Click Plus Icon on the Messaging Menu
    [Arguments]                                               ${input_emulator}
    :FOR        ${device}       in                            @{devices}
    \ Click Element                                             resourceId=com.android.messaging:id/start_new_conversation_button     device=${emulator}

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
    Reset App                                                     device=${emulator}    package=${apk}
    # Open App                                                      device=@{emulator}     package=${apk}
    # Click Element                                                 className=android.widget.TextView     devices_parallel=@{emulator}    index=0  text=Messaging
    # Click Element                                                 resourceId=com.android.messaging:id/start_new_conversation_button     devices_parallel=@{emulator}
    # Scan Device and Open Application Messaging                ${emulator}       ${apk}
    # Click Plus Icon on the Messaging Menu
    # Type Sender Number                                        ${sender_number}
    # Press Enter
    # Input Message on the Text Area                            ${message}
    # Click Button Send
    # Page Should Contain Text                                  text=${message}
    # Quit App                                                  ${emulator}       ${apk}
    # Close App
