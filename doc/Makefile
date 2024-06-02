## Copyright (C) 2024 Jim Newton

all: pdf

SRC_DIR  := .
IMAGE_DIR := $(SRC_DIR)/img
LATEXMK = latexmk -pvc --pdf

pdf: mgs-2024-handout.pdf mgs-2024-slides.pdf

mgs-2024-slides.pdf : ${SRC_DIR}/mgs-2024-slides.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/mgs-2024-slides.ltx
	([ -d ~/Google\ Drive/MGS\ 2024/. ] && cp -fv $@ ~/Google\ Drive/MGS\ 2024/.) || true

mgs-2024-handout.pdf : ${SRC_DIR}/mgs-2024-handout.ltx
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/mgs-2024-handout.ltx
	([ -d ~/Google\ Drive/MGS\ 2024/. ] && cp -fv $@ ~/Google\ Drive/MGS\ 2024/.) || true

pvc-handout:
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} --pdf ${SRC_DIR}/mgs-2024-handout.ltx

pvc-slides:
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} --pdf ${SRC_DIR}/mgs-2024-slides.ltx
