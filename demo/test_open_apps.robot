*** Settings ***
Library    ../mykonos/

*** Variables ***
${emulator}               192.168.56.103:5555
${apk}                    kudo.mobile.app.test/kudo.mobile.app.onboarding.FirstInstallTutorialActivity_
${element_locator}        android.widget.Button
${email}                  dedy.suryadi@kudo.co.id
${password}               Testing@123

*** keywords ***
Scan Device and Open Aplication
    ${device}=  Scan Current Device           ${emulator}
    Open Application                          ${emulator}     ${apk}

Click Slide Lanjut and Mengerti
    : FOR         ${index}          IN RANGE       0    3
    \             Click Element                             text=LANJUT

    Click Element                                           text=MENGERTI

Click Mengerti on Popup Root
    Click Element                                           text=MENGERTI

Click Button Masuk Sebagai Agent
    Click Element                                           text=MASUK SEBAGAI AGEN

Input HP or Email
    [Arguments]                                             ${input_hp_email}
    Input Text                                              input=${input_hp_email}   resourceId=kudo.mobile.app.test:id/activity_login_et_username

Click Button Mulai Berjualan
    Click Element                                           text=Mulai Berjualan

Input Password
    [Arguments]                                             ${input_password}
    Input Text                                              input=${input_password}     resourceId=kudo.mobile.app.test:id/login_et_password

Click Masuk as Agent
    Click Element                                           text=MASUK

*** Test Cases ***
Test Open Apps
  Scan Device and Open Aplication
  Click Slide Lanjut and Mengerti
  # Click Mengerti on Popup Root
  Click Button Masuk Sebagai Agent
  Input HP or Email                                       ${email}
  Click Button Mulai Berjualan
  Input Password                                          ${password}
  Click Masuk as Agent
