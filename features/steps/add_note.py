from behave import given, when, then
from application.tests.bdd.user import UserFactory
from application.tests.bdd.note import NoteFactory

import time

@given('a logged in user who is going to add a note')
def step_impl(context):
    u = UserFactory(username='asia', email='asia@example.com')
    u.set_password('password333')
    u.save()

    

    br = context.browser
    br.get(context.base_url + '/login/')

    br.find_element_by_name('username').send_keys('asia')
    br.find_element_by_name('password').send_keys('password333')
    br.find_element_by_id('login').click()


@when('I try to add a note')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_css_selector('#add-note') is not None
    br.find_element_by_css_selector('#add-note').click()


@then('I am redirected to the add note page')
def step_impl(context):
    br = context.browser
    print(br.current_url)

    assert br.current_url.endswith('/notes/add/')

    br.find_element_by_name('title').send_keys('testtitle')
    br.find_element_by_name('content').send_keys('testcontent')

    assert br.find_element_by_name('title') is not None
    assert br.find_element_by_name('content') is not None




@given('a logged in user who is going to add a note and see it')
def step_impl(context):
     u = UserFactory(username='tola', email='tola@example.com')
     u.set_password('password333')
     u.save()

    

     br = context.browser
     br.get(context.base_url + '/login/')

     br.find_element_by_name('username').send_keys('tola')
     br.find_element_by_name('password').send_keys('password333')
     br.find_element_by_id('login').click()

    

@when('I try to add a note with content')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_css_selector('#add-note') is not None
    br.find_element_by_css_selector('#add-note').click()
    assert br.current_url.endswith('/notes/add/')

    br.find_element_by_name('title').send_keys('testtitle')
    br.find_element_by_name('content').send_keys('testcontent')
    br.find_element_by_id('add').click()
    

@then('I see new note')
def step_impl(context):
    br = context.browser

    assert br.current_url.endswith('/application/')
    assert br.find_element_by_id("note-wrapper") is not None
    assert "testtitle" in br.find_element_by_id("note-wrapper").text
    assert "testcontent" in br.find_element_by_id("note-wrapper").text
    
    

