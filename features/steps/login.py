from behave import given, when, then
from application.tests.bdd.user import UserFactory


@given('an anonymous user')
def step_impl(context):
    u = UserFactory(username='fooooo', email='foo@example.com')
    u.set_password('password1234')
    u.save()


@when('I submit a valid login and password')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/login/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('username').send_keys('fooooo')
    br.find_element_by_name('password').send_keys('password1234')
    br.find_element_by_id('login').click()


@then('I see user page with add notes button')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_id('add-note') is not None
    assert br.current_url.endswith('/application/')


@when('I submit an invalid login and password')
def step_impl(context):
    br = context.browser

    br.get(context.base_url + '/login/')

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar-is-invalid')
    br.find_element_by_id('login').click()


@then('I am redirected to the login page')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_id('login') is not None
    assert br.find_element_by_id('register') is not None

