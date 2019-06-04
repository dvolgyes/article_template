#!/usr/bin/make

GLD={{cookiecutter.gitlatexdiff}}
GLD_OPTIONS={{cookiecutter.gitlatexdiff_options}}
TEXBASE=article
TEXENGINE={{cookiecutter.tex_engine}}
BIBENGINE={{cookiecutter.bib_engine}}

pdf:
	@mkdir -p build
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex
	${BIBENGINE} ${TEXBASE}
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex
	${TEXENGINE} -halt-on-error -interaction=batchmode ${TEXBASE}.tex
	@rm -f article.log article.aux article.aux article.log
	@mv article.pdf build

diff: pdf
	${GLD} ${GLD_OPTIONS} --main ${TEXBASE}.tex  HEAD~1 --

submission: pdf figures-zip tables-zip
	@mkdir -p submission
	@latexpand article.tex >submission.tex
	@zip -j -r submission/submission.zip figs/* figures/* tables/* submission.tex *.bst *.sty *.bib
	@cp build/*pdf submission/submission.pdf

figures-zip:
	@cd figs && zip -r -j ../figures.zip . || echo "There are no figures, no figures.zip is generated."

tables-zip:
	@cd tables && zip -r -j ../tables.zip . || echo "There are no tables, no tables.zip is generated."

clean:
	@rm -fr build
	@mkdir -p build
	@rm -fr figures.zip tables.zip
	@rm -f article.log article.aux article.pdf article.aux article.log
