# Created by Moi at 10/3/2019
Feature: Steps feature file
  # Enter feature description here

  Scenario: step has correct name
    Given a new step
    When i am saving it
    Then the name must not be empty