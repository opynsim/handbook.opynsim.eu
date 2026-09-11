# Always prefer the local `.venv`
export PATH := .venv/bin:$(PATH)

.PHONY: html livehtml clean

html:
	sphinx-build -b html "source/" "build/"

livehtml:
	sphinx-autobuild --open-browser --delay 1 "source/" "build/html"

clean:
	rm -rf "build"
