import click

@click.group()
def main():
pass

@main.command()
@click.argument('file')
def create(file):
  f= open(file,"w+")
  n=int(input("Enter the no. of lines : "))
  click.echo("Enter the contents of the file :")
  for i in range(n):
    write=input()
    f.write(write+"\n")
    f.close()

@main.command()
@click.argument('file')
def edit(file):
  f=open(file, "a+")
  n=int(input("Enter the no. of lines : "))
  click.echo("Enter the contents :")
  for i in range(n):
  write=input()
  f.write(write+"\n")
  f.close()

@main.command()
@click.argument('file')
def read(file):
  f=open(file, "r")
  contents =f.read()
  print(contents)

if __name__ == "__main__":
main()
