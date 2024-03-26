Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM website
    Given User launches the Chrome browser
    When User opens OrangeHRM homepage
    And User enters username "admin" and password "admin123"
    And User clicks login button
    Then User successfully logins to the dashboard