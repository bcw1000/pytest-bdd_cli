import os
import subprocess

import click

@click.group()
def pytest_bdd():
    """A set of tools to create and use pytest-bdd."""

# pytest-bdd generate test/feature/establish_environment.feature
@click.option('f', '--feature_file_spec', required=True, help='pathspec/full_filename of the feature file')
@pytest_bdd.command()
def pytest_from_gherkin(feature_file: str):
    """Generate Python stubs from a Gherkins file"""
    output = subprocess.check_output(['pytest_bdd', 'generate', ''.format(feature_file)])
    click.echo('Generated stubs:')
    click.echo(output)



# @click.option('-a', '--target_account', required=True, help='Root account in which to deploy the stack')
# @click.option('-f', '--accounts_file', required=True, help='Path and name of file containing account details')
# @pytest_bdd.command()
# def create_account(target_account: str, accounts_file: str):
#     """Create an SSO account from parameters listed in a file."""
#     click.echo('received {}, {}'.format(target_account, accounts_file))
#     # Provision the inputs
#     import subprocess
#     response = sts_client.get_caller_identity(
#     )
#     click.echo('AWS account configured in current shell environment: {}'.format(response['Account']))
    
#     # call the CDK tool to create the accounts
#     output = subprocess.check_output(['cdk', 'deploy', '-c', 'target_account={}'.format(target_account), '-c', 'accounts_file={}'.format(accounts_file)])
#     click.echo('Deployed CF template:')
#     click.echo(output)


# @click.option('-f', '--first_name', required=True, help='First or Given name of the user')
# @click.option('-s', '--surname', required=True, help='Surname of the user')
# @click.option('-e', '--email', required=True, help='Email address of the user')
# @click.option('-r', '--role', required=True, help='The role of the user, e.g. "Developer"')
# @pytest_bdd.command()
# def create_user(first_name: str, surname: str, email: str, role: str ):
#     """Create an SSO user."""
#     click.echo('received {}, {}, {}, {}'.format(first_name, surname, email, role))


# @click.option('-r', '--root_sso_email', required=True, help='Programmatically set the initial common root SSO email for this organisation, e.g. "aws+ct@domainename"')
# @pytest_bdd.command()
# def configure(root_sso_email: str):
#     """Script to configure common SSO requirements."""
#     click.echo('received {}'.format(root_sso_email))
#     response = sts_client.get_caller_identity()
#     click.echo('Configured AWS account: {}'.format(response['Account']))

#     response = ssm_client.put_parameter(Name='root_sso_email', Value='{}'.format(root_sso_email), Type='String', Overwrite=True)
#     if '200' != '{}'.format(response['ResponseMetadata']['HTTPStatusCode']):
#         click.echo('Failure! put_parameter response is: {}'.format(response))
#     else:
#         click.echo('SSM put_parameter response is HTTPStatusCode: {}'.format(response['ResponseMetadata']['HTTPStatusCode']))


# @pytest_bdd.command()
# def interactive_configure():
#     """Interactively configure common SSO requirements."""
#     response = sts_client.get_caller_identity()
#     click.echo('Configured AWS account: {}'.format(response['Account']))

#     # Provision the inputs
#     response = ssm_client.get_parameter(Name='root_sso_email')
#     configured_root_sso_email = '{}'.format(response['Parameter']['Value'])

#     value = click.prompt('Please enter root_sso_email', default=configured_root_sso_email)

#     if value != configured_root_sso_email:
#         response = ssm_client.put_parameter(Name='root_sso_email', Value=value, Type='String', Overwrite=True)
#         if '200' != '{}'.format(response['ResponseMetadata']['HTTPStatusCode']):
#             click.echo('Failure! put_parameter response is: {}'.format(response))
#         else:
#             click.echo('SSM put_parameter response is HTTPStatusCode: {}'.format(response['ResponseMetadata']['HTTPStatusCode']))
#     else:
#         click.echo('value is unchanged')



if __name__ == '__main__':
    pytest_bdd(prog_name='pytest_bdd')
