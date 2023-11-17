from just_count import count_count
import click

@click.command()
@click.argument("number", type = int)
def square(number):
    return count_count.main(number)

if __name__ == "__main__":
    square()

