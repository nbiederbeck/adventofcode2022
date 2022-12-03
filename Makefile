all: $(shell seq 3)
	./aoc 1 2
	python py/3.py

%: build/%
	@#

build/%:
	curl \
		--silent \
		https://adventofcode.com/2022/day/$*/input \
		--cookie "session=$$AOC_SESSION" \
		--output $@ \
		--create-dirs

clean:
	rm -rf build

.PHONY: all clean

.SECONDARY:
