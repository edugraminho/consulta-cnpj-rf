*** Settings ***
Documentation    Arquivo de recursos
Resource    ${ROOT}/Resources/main.resource


*** Tasks ***
Abrir Browser
    [Documentation]    Task que abre o browser e retorna seu status
    ${status}    Run Keyword And Return Status    Abrir Navegador    ${URL}    ${DOWNLOAD_DIRECTORY}
    IF    ${status}
        Set Next Task    Efetuar O Download Dos Dados

    ELSE
        Set Next Task    Finaliza Processo
    END

Efetuar O Download Dos Dados

    ${status}    Aguardar Pagina Carregar
    IF    ${status}
        Efetuar O Download Dos Dados Abertos
        # Click Element    xpath://a[contains(., "Dados Abertos CNPJ EMPRESA 01")]

        Set Next Task    Finaliza Processo
    ELSE
        Set Next Task    Finaliza Processo
    END


    
Finaliza Processo
    [Documentation]    Task de finalização do robô

    #TODO limpar Pasta de Downloads
    Log    Finalizando Processo!    level=INFO
    Fechar Navegador