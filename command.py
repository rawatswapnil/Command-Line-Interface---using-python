import click
import glob, os 
@click.group()
def main():
  pass

@main.command()
def cls():
  os.system("cls")
  
@main.command()
@click.argument('col')
def color(col):
  os.system("color "+col)
  
@main.command()
def date():
  os.system("date")

@main.command()
def hostname():
  os.system("hostname")
  
@main.command()
def tasklist():
  os.system("tasklist")
  
@main.command()
def ver():
  os.system("ver")

@main.command()
def time():
  os.system("time")

@main.command()
def getmac():
  os.system("getmac")

@main.command()
def ipconfig():
  os.system("ipconfig")

@main.command()
def vol():
  os.system("vol")

if __name__ == "__main__":
main()
