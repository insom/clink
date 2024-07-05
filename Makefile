.PHONY: all
all:
	venv/bin/python3 build.py
	zola build
	rsync -Pr public/ www@doorstep.insom.me.uk:/var/www/www.insom.me.uk/C/
