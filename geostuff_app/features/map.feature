
Feature: Map feature file
   Scenario: Step api allow creating map
    Given i am not an identified user
    When calling the latest version of the api to create a map
    Then i receive the newly created map
