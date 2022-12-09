Feature: MailSend
  # An authorized user should be able to send and receive messages

  Scenario Outline: SendToSelf
    Given I'm authenticated user on inbox page
    When I click on Write button
    And I fill Email field with user's email
    And I fill Subject field with <subject>
    And I fill Body field with <body>
    And Click Send button
    And I should see a message that the letter has been sent

    Examples:
      |subject       |body                 |
      |Приветствие   |Привет, как дела?    |

