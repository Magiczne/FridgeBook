Feature: Delete note

  Scenario: Deny the delete attempt when user is not the owner of a note

    Given a logged in user who is not the owner of a note
    When I try to delete a note which is not mine
    Then I am redirected to the main page and the note is not deleted

  Scenario: Deleting a note is successful

    Given a logged in user who is the owner of a note
    When I try to delete a note
    Then I am redirected to the main page and the note is deleted


