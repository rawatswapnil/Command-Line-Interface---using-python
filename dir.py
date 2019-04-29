import click
import glob, os

@click.group()
def main():
  pass

@main.command()
@click.argument('add')
def ls(add):
  os.chdir(add)
  for file in glob.glob("*.*"):
    click.echo(file)

@main.command()
def pwd():
  dirpath = os.getcwd()
  click.echo("current directory is : " + dirpath)
  foldername = os.path.basename(dirpath)
  click.echo("Directory name is : " + foldername)

@main.command()
@click.argument('add')
def ch(add):
  retval=os.getcwd()
  click.echo("Current working directory " + retval)
  os.chdir(add)
  retval=os.getcwd()
  click.echo("Directory changed successfully " + retval)

if __name__ == "__main__":
main()
