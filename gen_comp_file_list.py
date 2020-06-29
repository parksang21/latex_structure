from glob import glob
import sys, os

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('usage: python3 gen_comp_file_list generated_lg_files GT_lg_files')
        exit()

    gen_dir = sys.argv[1]
    label_dir = sys.argv[2]

    gen_fns = []
    gen_fns_ = glob(os.path.join(gen_dir, '*'))
    for fn in gen_fns_:
        gen_fns.append(os.path.basename(fn))

    label_fns = glob(os.path.join(label_dir, '*'))

    cnt = 0

    with open('lg_file_list.txt', 'w') as f:
        for fn in label_fns:
            fn = os.path.basename(fn)

            if fn in gen_fns:

                f.write(os.path.join(label_dir, fn) + ',' + os.path.join(gen_dir, fn) + '\n')
            else:
                # cnt indicates non-math tag in generated mml file
                cnt += 1
                print(fn)

    print('{} / {} files do not contain label graph'.format(cnt, len(label_fns)))
