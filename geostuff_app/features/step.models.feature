# Created by Moi at 10/3/2019
Feature: Steps feature file
  # Enter feature description here

############
  Scenario: step has correct name
    Given a new step
    When i am saving it
    Then the name must not be empty

  Scenario: Step api return all steps
    Given i am not an identified user
    When calling the latest version of the api
    Then i receive all existing step

  Scenario: Step api return specified step
    Given i am not an identified user
    And i created a new step
    When calling the latest version of the api with the step id
    Then i receive the specified step

  Scenario: Step api allow creating step
    Given i am not an identified user
    When calling the latest version of the api to create a step
    Then i receive the newly created step

  Scenario: Step api allow updating step
    Given i am not an identified user
    When calling the latest version of the api to update a step
    Then i receive the updated version of the step

