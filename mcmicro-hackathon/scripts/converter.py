import click


@click.command()
@click.option("--input-file", "-i", multiple=True, type=click.Path())
@click.option("--output-file", "-o", type=click.Path())
@click.option("--process-name", "-p")
def convert(input_file, output_file, process_name):
    click.echo("spatialdata-mcmicro: success!")
    click.echo(
        f'input_files: {", ".join(input_file)}\n'
        + f"output_file: {output_file}\n"
        + f"process_name: {process_name}"
    )
    if process_name == "illumination":
        from illumination.ashlar import convert

        convert(input_file, output_file)


if __name__ == "__main__":
    convert()
