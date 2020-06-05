Feature: View previous notes

  Scenario: Grant access to previous notes

    Given a logged in user who is an owner of notes
    When I am on the main page
    Then I see all my previous notes

  Scenario: See all of the notes

    Given two users with their notes
    When I am logged in
    Then I see all of the notes


