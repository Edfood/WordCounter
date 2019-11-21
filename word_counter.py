from collections import defaultdict
from pyknp import Jumanpp
import sys


def main():
    if len(sys.argv) != 2:
        print('need one argument for a file.')
        return

    file_name = sys.argv[1]
    vocab_dict = defaultdict(int)
    juman = Jumanpp()

    with open(file_name, 'r', encoding='utf-8', newline='') as fr:
        text = fr.readlines()

        for line in text:
            # juman++ doesn't support half-width character
            line = line.replace(' ', '　')
            line.translate(str.maketrans(
                {chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
            analysis = juman.analysis(line.replace('\n', ''))
            for m in analysis.mrph_list():
                vocab_dict[str(m.midasi)] += 1

    sorted_dict = sorted(vocab_dict.items(), key=lambda x: x[1], reverse=True)

    print(sorted_dict)
    print(len(sorted_dict))


if __name__ == "__main__":
    main()
