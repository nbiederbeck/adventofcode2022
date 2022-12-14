all: $(shell seq 14)
	./aoc.lua 1 2
	./aoc.py $^

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
