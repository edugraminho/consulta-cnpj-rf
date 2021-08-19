*** Settings ***
Documentation    Biblioteca responsável por toda navegação do menu lateral
Resource    ${ROOT}/Resources/main.resource


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
    Wait Until Element Is Visible    ${navegacao.btn_cookie}
    Click Element    ${navegacao.btn_cookie}
    ${status}    Run Keyword And Return Status    Wait Until Element Is Visible    ${navegacao.header}    timeout=2

    [Return]    ${status}


Efetuar O Download Dos Dados Abertos
    FOR    ${index}    IN RANGE    1    99
        ${link_download}    Format String    ${navegacao.link_download}    index=${index}

        Log    Iniciando o loop de clicks no elemento ${link_download}
        
        ${status}    Run Keyword And Return Status    Wait Until Element Is Visible    ${link_download}    timeout= 3
        Run Keyword If    ${status}    Scroll Element Into View    ${link_download}
        Run Keyword If    ${status}    Click Element    ${link_download}
        ${file_name}    Get Text    ${link_download}
        Set Selenium Speed    200
        Aguardar Download Ser Concluido    ${file_name}

        Exit For Loop If    ${status} == ${False}
    END


Aguardar Download Ser Concluido
    [Documentation]    Verifies that the directory has only one folder and it is not a temp file.
    [Arguments]    ${file_name}

    ${files}    List Files In Directory    ${DOWNLOAD_DIRECTORY}

    Log    ${files}
    FOR    ${file}    IN    @{files}
        ${status}    Evaluate    '${file}'.endswith("load") or '${file}'.endswith("tmp")

        IF    ${status}
            Log    Esperando Download ser Concluído: ${file_name}    console=True
            ${tmp_file}    Join Path    ${DOWNLOAD_DIRECTORY}    ${file}
            Wait Until Removed    ${tmp_file}    timeout=10 minute
        END
        
    END

    # Log    File was successfully downloaded to ${file}
    # [Return]    ${file}