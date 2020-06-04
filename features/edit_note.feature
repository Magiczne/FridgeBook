Feature: Edit note form

  Scenario: Grant an access to the edit note page

    Given a logged in user who is an owner of a note
    When I try to edit a note
    Then I am redirected to the edit note page

  Scenario: Deny an access to the edit note page when user is not an owner of a note

    Given a logged in user who is not an owner of a note
    When I try to edit a note which is not mine
    Then I am redirected to the main page

  Scenario: Editing a note is successful

    Given a logged in user who is an owner of a note
    When I try to edit a note with content
    Then I am redirected to the main page


