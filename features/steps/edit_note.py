from behave import given, when, then

from application.tests.bdd.note import NoteFactory
from application.tests.bdd.user import UserFactory


@given('a logged in user who is an owner of a note')
def step_impl(context):
    u = UserFactory(username='alaala', email='ala@example.com')
    u.set_password('password333')
    u.save()

    n = NoteFactory(title='my note', content='note content', user=u)
    n.save()

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('alaala')
    br.find_element_by_name('password').send_keys('password333')
    br.find_element_by_id('login').click()


@when('I try to edit a note')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_css_selector('#edit-note') is not None
    br.find_element_by_css_selector('#edit-note').click()


@then('I am redirected to the edit note page')
def step_impl(context):
    br = context.browser
    print(br.current_url)

    assert br.current_url.endswith('/notes/edit/4')
    assert br.find_element_by_name('title') is not None
    assert br.find_element_by_name('content') is not None


@given('a logged in user who is not an owner of a note')
def step_impl(context):
    u = UserFactory(username='alaala', email='ala@example.com')
    u.set_password('password333')
    u.save()

    n = NoteFactory(title='my note', content='note content', user=u)
    n.save()

    u = UserFactory(username='alaola', email='alaola@example.com')
    u.set_password('password333')
    u.save()

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('alaola')
    br.find_element_by_name('password').send_keys('password333')
    br.find_element_by_id('login').click()


@when('I try to edit a note which is not mine')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/application/notes/edit/5')


@then('I am redirected to the main page')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/application/')


@when('I try to edit a note with content')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/application/notes/edit/6')

    br.find_element_by_name('title').send_keys('new title')
    br.find_element_by_name('content').send_keys('new content')
    br.find_element_by_id('edit').click()
