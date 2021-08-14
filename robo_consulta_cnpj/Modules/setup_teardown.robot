*** Settings ***
Documentation    Keywords de setup e teardown
Resource    ${ROOT}/Resources/main.resource


*** Keywords ***
Inicializando Processos
    Pasta GDrive Disponivel
    Create Directory    ${DOWNLOAD_DIRECTORY}
    Empty Directory    ${DOWNLOAD_DIRECTORY}
    Open Connections
    
Finalizando Processos
    Fechar Navegador
    Close Connections
