from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException

from application.tests.bdd.note import NoteFactory
from application.tests.bdd.user import UserFactory


@given('a logged in user who is not the owner of a note')
def step_impl(context):
    u = UserFactory(username='filip', email='filip@example.com')
    u.set_password('password333')
    u.save()

    n = NoteFactory(title='note to delete', content='note content', user=u)
    n.save()

    u = UserFactory(username='filip1', email='filip1@example.com')
    u.set_password('password333')
    u.save()

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('filip1')
    br.find_element_by_name('password').send_keys('password333')
    br.find_element_by_id('login').click()


@when('I try to delete a note which is not mine')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('note to delete') is not None
    assert_no_element_of_id(br, 'delete-note-link2')
    br.get(context.base_url + '/application/notes/delete/2')


@then('I am redirected to the main page and the note is not deleted')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/application/')
    assert br.find_element_by_id('note to delete') is not None


@given('a logged in user who is the owner of a note')
def step_impl(context):
    u = UserFactory(username='filip', email='filip@example.com')
    u.set_password('password333')
    u.save()

    n = NoteFactory(title='note to delete', content='note content', user=u)
    n.save()

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('filip')
    br.find_element_by_name('password').send_keys('password333')
    br.find_element_by_id('login').click()


@when('I try to delete a note')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('note to delete') is not None
    assert br.find_element_by_id('delete-note-link3') is not None

    br.find_element_by_id('delete-note-link3').click()


@then('I am redirected to the main page and the note is deleted')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/application/')
    assert_no_element_of_id(br, 'note to delete')
    assert_no_element_of_id(br, 'delete-note-link3')


def assert_no_element_of_id(br, id):
    no_element = False
    try:
        br.find_element_by_id(id)
    except NoSuchElementException:
        no_element = True
    assert no_element
