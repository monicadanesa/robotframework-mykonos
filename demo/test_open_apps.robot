*** Settings ***
Library    ../mykonos/

*** Variables ***
${emulator}               emulator-5554
${apk}                    sample app
${element_locator}        sample locator

*** keywords ***
Scan Device and Open Aplication
    ${device}=  Scan Current Device           ${emulator}
    Open Application                          ${emulator}     ${apk}
