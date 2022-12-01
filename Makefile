%: puzzles/day%.txt
	@lua day$*.lua

puzzles:
	mkdir -p $@

puzzles/day%.txt: | puzzles
	curl \
		--silent \
		https://adventofcode.com/2022/day/$*/input \
		--cookie "session=$$AOC_SESSION" \
		--output $@

clean:
	rm -rf puzzles

.PHONY: clean
