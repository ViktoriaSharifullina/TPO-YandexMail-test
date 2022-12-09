Feature: MailAuth

#  Scenario Outline: RegisteredLogin
#    Given I'm on the login page
#    When I select email as login type
#    And I enter user's email <email>
#    And I click on first button
#    And I enter user's password <password>
#    And I click on second button
#    Then I should see user's Inbox page
#
#    Examples:
#      | email                    | password   |
#      | mietpythontest@yandex.ru | 2323test   |


#  Scenario Outline: LoginStranger
#    Given I'm on the login page
#    When I select email as login type
#    And I enter stranger's email <email>
#    And I click on login button
#    Then I should see NoUserExists message
#
#    Examples:
#      | email         |
#      | aergergrgagrr |


  Scenario Outline: LoginRegisteredWrongPass
    Given I'm on the login page
    When I select email as login type
    And I enter user's email <email>
    And I click on first button
    And I enter <something> which is not user's password
    And I click on second button
    Then I should see WrongPassword message

    Examples:
      | something  | email                    |
      | 1234567890 | mietpythontest@yandex.ru |

#
#  Scenario: LogOut
#    Given I'm authenticated user on inbox page
#    When I click on my profile picture
#    And Click on LogOut
#    Then I should not see user's Inbox page
#
#  Scenario: LoginEmptyInputEmail
#    Given I'm on the login page
#    When I select email as login type
#    And I don't enter user's email
#    And I click on login button
#    Then I should see message about empty field
#
#  Scenario: LoginEmptyInputPhone
#    Given I'm on the login page
#    When I select phone as login type
#    And I don't enter user's phones
#    And I click on login button
#    Then I should see message about empty field
#
#
#  Scenario Outline: PhoneStranger
#    Given I'm on the login page
#    When I select phone as login type
#    And I enter stranger's phone <phone>
#    And I click on login button
#    Then I should see message about phone's format
#
#    Examples:
#      | phone         |
#      | 3463876483768 |
