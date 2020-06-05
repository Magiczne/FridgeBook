Feature: Mark note as read

  Scenario: Note after marking it is as read is opaque-looking

    Given a logged in user who is an owner of notes
    When I am on the main page
    And I mark the note as read
    Then The note is properly marked as read
