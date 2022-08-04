@Web @HappyPath @Regression
Feature: Task creation
  As a ToDo App user
  I should be able to create a subtask
  So I can break down my tasks into smaller pieces

  Background: User logs in into the ToDo App
    Given I have the endpoint "https://qa-test.avenuecode.io/"
    And I have the user email "gabriel_aguido@hotmail.com"
    And I have the user password "Quality2022"
    Then I should be able to login
    And I should be able to create a new task

  Scenario: Create subtask
    Given I create a subtask
    Then I can see the subtask created