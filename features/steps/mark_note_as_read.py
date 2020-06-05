from behave import when, then


@when('I mark the note as read')
def step_impl(context):
    br = context.browser

    br.find_element_by_id('My first note').click()


@then('The note is properly marked as read')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_css_selector('.note.note-read') is not None
