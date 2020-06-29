from glob import glob
import sys
import os

"""
convert output txt file to tex format

usage: python3 txt2tex.py output_text_file save_dir_path
example: python3 txt2tex.py ../result/test_decode_result.txt ./test_tex_result/
"""


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python3 txt2tex.py output_text_file save_dir_path')
        exit()

    output_txt = sys.argv[1]
    save_dir = sys.argv[2]

    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    with open(output_txt, 'r') as f:
        data = f.readlines()
    
    for l in data:
        # delete "\n" charactor
        l = l[:-1]

        l_ = l.split('\t')
        save_fn = os.path.join(save_dir, l_[0] + '.txt')
        save_data = ' '.join(l_[1:])
    
        with open(save_fn, 'w') as f:
            f.write('\\begin{equation}\n\t' + save_data + '\n\\end{equation}')
