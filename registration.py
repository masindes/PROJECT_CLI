import click
import sqlite3

@click.group()
@click.version_option(version='8.1.7', prog_name='Registration')
def main():
    """Simple Registration CLI"""
    pass




if __name__ == "__main__":
    main()
