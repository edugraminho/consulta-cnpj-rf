*** Settings ***
Library    SeleniumLibrary
Library    DebugLibrary
Library    String
Library    Collections
Library    OperatingSystem
Library    DateTime
Library    RPA.Tasks


#========= Custom Libraries ==========
Library    ${ROOT}/Libraries/chromedriver_utils.py
Library    ${ROOT}/Libraries/utils.py

#========= Keywords ==========
Resource    ${ROOT}/Modules/navegacao.robot
Resource    ${ROOT}/Modules/setup_teardown.robot

#========= Locators ==========
Resource    ${ROOT}/Resources/navegacao.resource

#========= Connections ==========
Library    ${ROOT}/Libraries/Connections/MongoLibrary.py


# #========= Variables ==========
# Resource    ${ROOT}/Variables/config.py