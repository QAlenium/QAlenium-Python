@Web @HappyPath @Regression
Feature: Task creation
  As a ToDo App user
  I should be able to create a task
  So I can manage my tasks

  Background: User logs in into the ToDo App
    Given I have the endpoint "https://website/"
    And I have the user email "email@provider.com"
    And I have the user password "password"
    Then I should be able to login

  Scenario: Create task
    Given I access the "My Tasks" menu
    And I can see "Hey USERNAME, this is your todo list for today:"
    When I create a new task
    Then I can see the created task in the list

  Scenario Outline: Invalid task creation
    Given I access the "My Tasks" menu
    And I can see "Hey USERNAME, this is your todo list for today:"
    When I try to create a new task with "<number>" characters
    Then I should not be able to create it

    Examples:
      | number |
      | 2      |
      | 251    |
