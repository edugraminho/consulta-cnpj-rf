*** Settings ***
Documentation    Biblioteca responsável por toda navegação do menu lateral
Resource    ${ROOT}/Resources/main.resource

Library    String

*** Keywords ***
Fechar Navegador
    Close All Browsers

Abrir Navegador
    [Documentation]    Abre o navegador maximizado.
    ...    Escolhi este método por ter melhor performance e pela necessidade
    ...    de carregar uma extensão que desabilita os alertas Js.
    [Arguments]    ${URL}    ${download_dir}=${None}
    ${prefs}    Create Dictionary    download.default_directory=${download_dir}    plugins.always_open_pdf_externally=${True}
    ${options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_experimental_option    prefs    ${prefs}
    Call Method    ${options}    add_argument    start-maximized
    Call Method    ${options}    add_argument    disable-web-security
    Call Method    ${options}    add_argument    disable-notifications
    Call Method    ${options}    add_argument    disable-logging
    ${options.binary_location}    Browser Path
    ${chromedriver_path}    Chromedriver Path
    ${BrowserOpened}    Run Keyword And Return Status    Open Browser    ${URL}    Chrome    options=${options}    executable_path=${chromedriver_path}
    Set Selenium Timeout    ${DEFAULT_SELENIUM_TIMEOUT}
    [return]    ${BrowserOpened}


Aguardar Pagina Carregar
    Click Element    ${navegacao.btn_cookie}
    ${status}    Run Keyword And Return Status    Wait Until Element Is Visible    ${navegacao.header}

    [Return]    ${status}


Clicar Nos Links

    FOR    ${index}    IN RANGE    1    99
        ${link_download}    Format String    ${navegacao.link_download}    index=${index}

        Log    Iniciando o loop de clicks no elemento ${link_download}
        
#        ${status}    Run Keyword And Return Status    Click Element    ${link_download}
        ${status}    Run Keyword And Return Status    Wait Until Element Is Visible    ${link_download}    timeout= 3
        Run Keyword If    ${status}    Scroll Element Into View    ${link_download}

        Run Keyword If    ${status}    Click Element    ${link_download}

        Exit For Loop If    ${status} == ${False}
    END
