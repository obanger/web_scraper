import click
from tags_getter_and_reader.get_tags import TagsGetter
from tags_getter_and_reader.read_tags import TagsReader


@click.command()
@click.argument('web_site_name', required=False)
@click.option('--get', is_flag=True)
@click.option('--view', is_flag=True)
def cli(web_site_name, get, view):
    if web_site_name is None:
        print("web site URL is required")
    elif web_site_name is not None and get is True and view is True:
        print("Only one option is available")
    elif web_site_name and get is False and view is False:
        print("At least one parameter is required")
    elif get is True and view is False:
        print("Start scraper")
        TagsGetter(web_site_name).get_tags()
    elif get is False and view is True:
        print("Start read from DB")
        TagsReader(web_site_name).read_tags()


if __name__ == '__main__':
    cli()


#addedcomment