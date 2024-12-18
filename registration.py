import click
import sqlite3

@click.group()
@click.version_option(version='8.1.7', prog_name='Registration')
def main():
    """Simple Registration CLI"""
    pass

# add Patient 
@main.command()
@click.option('firstName', 'fn', required=True)
@click.option('lastName', 'ln', required=True)
@click.option('age', 'a', required=True)
@click.option('patientId', 'pi', required=True, default = None)
@click.option('PhoneNumber', 'pn', required=True, default = None)


def add_Patient():
    """Add a Patient Interactively or By specifying Ward name
    """


if __name__ == "__main__":
    main()
