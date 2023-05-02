Feature: verifying login page testcase

  Background:
    Given open newtours browser

  @smoke
  Scenario: login with valid username and password
    When provide valid username and password
    Then verify login is successfull or not

  @sanity
  Scenario: login with valid username and password with params
    When provide valid "mercury" and "mercury"
    Then verify login is successfull or not

  @regression
  Scenario Outline: verifying login page with valid and invalid username and password
    When provide valid "<userName>" and "<password>"
    Then verify success message in login home
    Examples:
      | userName | password |
      | mercury  | mercury  |
      | mercury  | &^%*((   |
      | 2342@#$  | mercury  |

  @lokesh
  Scenario: login with valid table formate params
    When verify with below query params
      | userName | password |
      | mercury  | mercury  |
    Then verify login is successfull or not