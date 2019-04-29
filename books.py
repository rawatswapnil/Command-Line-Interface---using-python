import click
import requests
@click.group()
def main():
pass
@main.command()
@click.argument('query')
def search(query):
7
url_format = 'https://www.googleapis.com/books/v1/volumes' query = "+".join(query.split())
query_params = {
'q': query
}
response = requests.get(url_format, params=query_params)
click.echo(response.json()['items'])
@main.command()
@click.argument('id')
def get(id):
url_format = 'https://www.googleapis.com/books/v1/volumes/{}' click.echo(id)
response = requests.get(url_format.format(id))
click.echo(response.json())
if __name__ == "__main__":
main()
