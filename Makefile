.PHONY: all
all:
	zola build
	rsync -Pr public/ www@doorstep.insom.me.uk:/var/www/www.insom.me.uk/C/
