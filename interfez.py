#-*- coding: utf-8 -*-
import click

@click.command()
@click.option('--contar', default = 1,
	help = u"Número de saludos")
@clicl.option('--nombre', prompt='Tu nombre',
	help = 'La persona a saludar')
def hello(contar, nombre):
	for x in range(contar):
		click.echo('hola %s' % nombre)

if __name__ == '__main__':
	hello()