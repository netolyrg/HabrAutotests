from page_objects.feedback_page import FeedbackPage


def test_errors_on_empty_fields(feedback_page: FeedbackPage):
    feedback_page.submit_button.click()

    checks = [
        feedback_page.email_error_message.is_displayed(),
        feedback_page.email_error_message.is_displayed(),
        feedback_page.personal_agreement_error_message.is_displayed()
    ]

    assert all(checks), f'Some errors are not shown: {checks}'


def test_number_of_feedback_subjects(feedback_page: FeedbackPage):
    expected = 9
    actual = feedback_page.count_subjects()

    assert actual == expected, f'Wrong subjects number: {actual}'


def test_change_subject(feedback_page: FeedbackPage):
    previous = feedback_page.subject.first_selected_option.text

    feedback_page.change_subject_by_index()

    current = feedback_page.subject.first_selected_option.text

    assert previous == current, f'Subject did not change. Prev: {previous}, current: {current}'

