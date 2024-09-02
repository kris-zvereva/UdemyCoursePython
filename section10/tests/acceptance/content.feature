Feature: Test that pages have the correct content
  Scenario: Blog page has the correct title
    Given I am on the blog page
    Then There is a title shown on the page
    And The title tag has content "This is the blog page"
