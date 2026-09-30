class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            j = i
            length = 0

            # Find how many words can fit in this line
            while j < len(words):
                if length + len(words[j]) + (j - i) > maxWidth:
                    break

                length += len(words[j])
                j += 1

            line_words = words[i:j]
            word_count = len(line_words)

            # Last line OR only one word
            if j == len(words) or word_count == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)

            else:
                # Total spaces needed
                total_spaces = maxWidth - length

                # Number of gaps
                gaps = word_count - 1

                spaces = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]

                    # Left gaps get extra spaces
                    line += " " * (spaces + (1 if k < extra else 0))

                line += line_words[-1]

                result.append(line)

            i = j

        return result
        