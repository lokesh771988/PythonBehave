Feature: Sample code testing

  Scenario: Opening google page and verify title
    Given Opening browser
    When Providing google url in browser
    Then Verify title of the google page
