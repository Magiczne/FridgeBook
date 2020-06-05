Feature: Add note form

  Scenario: Grant an access to the add note page

    Given a logged in user who is going to add a note
    When I try to add a note
    Then I am redirected to the add note page

   Scenario: Add note when user is logged in

    Given a logged in user who is going to add a note and see it
    When I try to add a note with content
    Then I see new note
