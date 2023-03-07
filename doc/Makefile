## Copyright (C) 2023 Jim Newton

all: pdf

SRC_DIR  := .
IMAGE_DIR := $(SRC_DIR)/img
LATEXMK = latexmk -pvc --pdf

pdf: mgs-2023-handout.pdf mgs-2023-slides.pdf

mgs-2023-slides.pdf : ${SRC_DIR}/mgs-2023-slides.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/mgs-2023-slides.ltx
	([ -d ~/Google\ Drive/MGS\ 2023/. ] && cp -fv $@ ~/Google\ Drive/MGS\ 2023/.) || true

mgs-2023-handout.pdf : ${SRC_DIR}/mgs-2023-handout.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/mgs-2023-handout.ltx
	([ -d ~/Google\ Drive/MGS\ 2023/. ] && cp -fv $@ ~/Google\ Drive/MGS\ 2023/.) || true

pvc-handout:
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} --pdf ${SRC_DIR}/mgs-2023-handout.ltx

pvc-slides:
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} --pdf ${SRC_DIR}/mgs-2023-slides.ltx
