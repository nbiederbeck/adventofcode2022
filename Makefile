all: $(shell seq 5)
	./aoc.lua 1 2
	./aoc.py 3 4 5

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
