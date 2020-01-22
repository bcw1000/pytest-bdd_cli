# pytest-bdd_cli
A pytest-bdd CLI tool in a Docker image
```
$ docker-compose -f ~/development/pytest-bdd_cli/docker-compose.yml run pytest-bdd_cli
Usage: pytest_bdd [OPTIONS] COMMAND [ARGS]...

  A set of tools to create and use pytest-bdd.

Options:
  --help  Show this message and exit.

Commands:
  pytest-from-gherkin  Generate Python stubs from a Gherkins file
```

```
  $ docker-compose -f ~/development/pytest-bdd_cli/docker-compose.yml run pytest-bdd_cli pytest-from-gherkin -f establish_environment.feature
Generated stubs:
# coding=utf-8
"""Establish resources needed to collect ChromeOS assets feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('input/establish_environment.feature', 'Create /opt/google when it already exists')
def test_create_optgoogle_when_it_already_exists():
    """Create /opt/google when it already exists."""

$ docker-compose -f ~/development/pytest-bdd_cli/docker-compose.yml run pytest-bdd_cli pytest-from-gherkin -f establish_environment.feature
Generated stubs:
# coding=utf-8
"""Establish resources needed to collect ChromeOS assets feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('input/establish_environment.feature', 'Create /opt/google when it already exists')
def test_create_optgoogle_when_it_already_exists():
    """Create /opt/google when it already exists."""


@scenario('input/establish_environment.feature', 'Create /opt/google when it does not exist')
def test_create_optgoogle_when_it_does_not_exist():
    """Create /opt/google when it does not exist."""


@given('an accessible /opt/google folder does not exist')
def an_accessible_optgoogle_folder_does_not_exist():
    """an accessible /opt/google folder does not exist."""
    raise NotImplementedError


@given('an accessible /opt/google folder exists')
def an_accessible_optgoogle_folder_exists():
    """an accessible /opt/google folder exists."""
    raise NotImplementedError


@when('I attempt to create opt/google folder')
def i_attempt_to_create_optgoogle_folder():
    """I attempt to create opt/google folder."" $ docker-compose -f ~/development/pytest-bdd_cli/docker-compose.yml run pytest-bdd_cli pytest-from-gherkin -f establish_environment.feature"
    raise NotImplementedError


@then('I receive confirmation the folder exists and is accessible')
def i_receive_confirmation_the_folder_exists_and_is_accessible():
    """I receive confirmation the folder exists and is accessible."""
    raise NotImplementedError

@scenario('input/establish_environment.feature', 'Create /opt/google when it does not exist')
def test_create_optgoogle_when_it_does_not_exist():
    """Create /opt/google when it does not exist."""


@given('an accessible /opt/google folder does not exist')
def an_accessible_optgoogle_folder_does_not_exist():
    """an accessible /opt/google folder does not exist."""
    raise NotImplementedError


@given('an accessible /opt/google folder exists')
def an_accessible_optgoogle_folder_exists():
    """an accessible /opt/google folder exists."""
    raise NotImplementedError


@when('I attempt to create opt/google folder')
def i_attempt_to_create_optgoogle_folder():
    """I attempt to create opt/google folder."""
    raise NotImplementedError


@then('I receive confirmation the folder exists and is accessible')
def i_receive_confirmation_the_folder_exists_and_is_accessible():
    """I receive confirmation the folder exists and is accessible."""
    raise NotImplementedError
```