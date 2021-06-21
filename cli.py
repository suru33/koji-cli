import click

from koji_ext import search


@click.command()
@click.argument('tag', type=click.STRING)
@click.option('--arch', type=str, default='aarch64')
def main(tag, arch):
    search(tag, arch)
