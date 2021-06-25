import os
import datetime
import multiprocessing


def parse(name, is_list: bool):
    config = "".join(open("config.txt", 'r', encoding='utf=8').readlines())
    parsed_list = config.replace('\n', "").split(name)[1].split('}')[0].split('{')[1].split('"')
    if not is_list:
        return parsed_list[0].strip()
    for i in range(0, len(parsed_list), 2):
        del parsed_list[i-int(i/2)]
    return parsed_list


def prepare(folder):
    files = parse("files", is_list=True)
    location = parse("location", is_list=True)
    exclude = parse("exclude_folder", is_list=True)
    cores = parse("cores", is_list=False)
    compress(folder, files, location, exclude, cores)


def compress(folder: str, files, location, exclude, cores):
    date = datetime.datetime.now().strftime('%y-%m-%d')
    name = folder.split('\\')[-1]
    if location[files.index(folder)] == "" and files.index(folder) != 0:
        i = files.index(folder)
        while i != -1:
            if location[i] == "":
                i -= 1
                continue
            location = location[i]
            break
    else:
        location = location[files.index(folder)]
    if not location.endswith("\\") and location != "":
        location += "\\"
    exclude_str = ""
    for string in exclude:
        exclude_str += f"-xr!{string} "
    os.system(f'7z a -t7z "{location}{date}\\{name}-{date}" "{folder}" -mmt{cores} -mx=1 {exclude_str}')


if __name__ == "__main__":
    folders = parse("files", is_list=True)
    pool = multiprocessing.Pool(len(folders))
    pool.map(prepare, folders)
    pool.close()
    pool.join()
