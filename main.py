import os
import datetime
import multiprocessing


def parse(name, is_list: bool):
    config = open("config.txt", 'r', encoding='utf=8')
    parsed_list = "".join(config.readlines()).replace('\n', "").split(name)[1].split('}')[0].split('{')[1].split('"')
    if not is_list:
        return parsed_list[0].strip()
    for i in range(0, len(parsed_list), 2):
        del parsed_list[i-int(i/2)]
    return parsed_list


def prepare(folder):
    cores = parse("cores", is_list=False)
    location = parse("location", is_list=True)
    compress(folder, cores, location)


def compress(folder: str, cores, location):
    date = datetime.datetime.now().strftime('%y-%m-%d')
    name = folder.split('\\')[-1]
    os.system(f'7z a "{location}{name}-{date}" "{folder}" -mmt{cores} -mx=1')


if __name__ == "__main__":
    folders = parse("files", is_list=True)
    pool = multiprocessing.Pool(len(folders))
    pool.map(prepare, folders)
    pool.close()
    pool.join()
