from playwright.sync_api import Page, expect


def test_todo_functionality(page: Page):
    page.goto('https://demo.playwright.dev/todomvc/#/')

    # Create a new todo item
    page.locator(".new-todo").fill("Learn Playwright")
    page.locator(".new-todo").press("Enter")

    # Verify the todo was added
    todo_items = page.locator(".todo-list li")
    expect(todo_items).to_have_count(1)
    expect(todo_items).to_have_text(["Learn Playwright"])

    # Mark todo as completed
    page.locator(".todo-list li .toggle").check()

    # Verify item is marked as completed
    expect(page.locator(".todo-list li")).to_have_class(["completed"])

    # Clear completed todos
    page.locator(".clear-completed").click()

    # Verify the list is empty
    expect(todo_items).to_have_count(0)
