*** Settings ***
Documentation    Arquivo de recursos
Resource    ${ROOT}/Resources/main.resource


*** Tasks ***
Abrir Browser
    [Documentation]    Task que abre o browser e retorna seu status
    ${status}    Run Keyword And Return Status    Abrir Navegador    ${URL}    ${DOWNLOAD_DIRECTORY}
    IF    ${status}
        Set Next Task    Carregar Pagina

    ELSE
        Set Next Task    Finaliza Processo
    END

Carregar Pagina

    ${status}    Aguardar Pagina Carregar
    IF    ${status}
        Log    Deu boa!!    console=True
        Clicar Nos Links
        Set Next Task    Finaliza Processo
    ELSE
        Set Next Task    Finaliza Processo
    END


    
Finaliza Processo
    [Documentation]    Task de finalização do robô
    Log    Finalizando Processo!    level=INFO
    Fechar Navegador
