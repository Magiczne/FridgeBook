from behave import given, when, then
from application.tests.bdd.user import UserFactory
from application.tests.bdd.note import NoteFactory

import time


@given('a logged in user who is an owner of notes')
def step_impl(context):
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('test123')
    u.save()

    n = NoteFactory(title='My first note', content='My first description', user=u)
    n.save()

    n = NoteFactory(title='My second note', content='My second description', user=u)
    n.save()

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('test123')
    br.find_element_by_id('login').click()


@when('I am on the main page')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_id('add-note') is not None
    assert br.current_url.endswith('/application/')


@then('I see all my previous notes')
def step_impl(context):
    br = context.browser

    assert "2" in br.find_element_by_id("notes-number").text
    assert br.find_element_by_id("note-wrapper") is not None
    assert "My first note" in br.find_element_by_id("note-wrapper").text
    assert "My first description" in br.find_element_by_id("note-wrapper").text
    assert "My second note" in br.find_element_by_id("note-wrapper").text
    assert "My second description" in br.find_element_by_id("note-wrapper").text


@given('two users with their notes')
def step_impl(context):
    u1 = UserFactory(username='foo', email='foo@example.com')
    u1.set_password('test123')
    u1.save()
    u2 = UserFactory(username='John', email='john@example.com')
    u2.set_password('john123')
    u2.save()

    n = NoteFactory(title='I am foo', content='I want to see your notes!', user=u1)
    n.save()

    n = NoteFactory(title='I am John', content='I want to see your notes too!', user=u2)
    n.save()

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('test123')
    br.find_element_by_id('login').click()


@when('I am logged in')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_id('add-note') is not None
    assert br.current_url.endswith('/application/')


@then('I see all of the notes')
def step_impl(context):
    br = context.browser

    assert "2" in br.find_element_by_id("notes-number").text
    assert br.find_element_by_id("note-wrapper") is not None
    assert "I am foo" in br.find_element_by_id("note-wrapper").text
    assert "I want to see your notes!" in br.find_element_by_id("note-wrapper").text
    assert "I am John" in br.find_element_by_id("note-wrapper").text
    assert "I want to see your notes too!" in br.find_element_by_id("note-wrapper").text

