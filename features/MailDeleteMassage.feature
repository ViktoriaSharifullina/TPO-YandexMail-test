Feature: MailDeleteMassage

  Scenario Outline: DeleteMessage
    Given I'm authenticated user on inbox page
    And I select my last message
    And Click on Delete button
    Then I should not see message with subject <subject>

    Examples:
      | subject        |
      | unique subject |