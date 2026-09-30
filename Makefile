PAPER_NAME := Litt_Problem_13_F4

.PHONY: all paper clean

all: paper

paper:
	mkdir -p build output/pdf
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build $(PAPER_NAME).tex
	cp build/$(PAPER_NAME).pdf output/pdf/$(PAPER_NAME).pdf
	sha256sum output/pdf/$(PAPER_NAME).pdf $(PAPER_NAME).tex > SHA256SUMS.txt

clean:
	latexmk -C -outdir=build $(PAPER_NAME).tex
