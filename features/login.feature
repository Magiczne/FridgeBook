Feature: Login form

  Scenario: Access the login form

	Given an anonymous user
	When I submit a valid login and password
	Then I see user page with add notes button

	Given an anonymous user
	When I submit an invalid login and password
	Then I am redirected to the login page