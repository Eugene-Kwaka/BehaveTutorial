Feature: OrangeHRM logo

  Scenario: Confirming the logo of the home page
    Given launch chrome browser
    When user opens Orangehrm homepage
    Then verify that logo is present
    And close browser