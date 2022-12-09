Feature: MailSearchMassage

  Scenario Outline: SearchMessage
    Given I'm authenticated user on inbox  page
    And I enter topic <topic> a message
    And Click on search button
    Then I should see message with this topic <topic>

    Examples:
      | topic       |
      | Приветствие |

  Scenario Outline: SearchMessage
    Given I'm authenticated user on inbox  page
    And I enter not existed topic <topic> a message
    And Click on search button
    Then I shouldn't see any messages about not existed messages

    Examples:
      | topic         |
      | unique  topic |