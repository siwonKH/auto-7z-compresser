import os
import datetime
import multiprocessing


def parse(name, is_list: bool):
    # reads texts
    config = "".join(open("config.txt", 'r', encoding='utf=8').readlines()).replace('\n', "")
    # parses object named {name}
    parsed_list = config.split(name)[1].split('}')[0].split('{')[1].split('"')
    # returns list or string, depends on parsing option
    if not is_list:
        return parsed_list[0].strip()

    for i in range(0, len(parsed_list), 2):
        del parsed_list[i-int(i/2)]
    return parsed_list


def prepare(folder):
    # parse configurations
    files = parse("files", is_list=True)
    location = parse("location", is_list=True)
    exclude = parse("exclude_folder", is_list=True)
    cores = parse("cores", is_list=False)
    # runs compress progress
    compress(folder, files, location, exclude, cores)


def compress(folder: str, files, location, exclude, cores):
    date = datetime.datetime.now().strftime('%y-%m-%d')
    name = folder.split('\\')[-1]
    # if location is blank, lookup latest location
    i = files.index(folder)
    while i != -1:
        if location[i] != "":
            location = location[i]
            break
        i -= 1
    # beautify form
    location = location.strip("\\")
    location += "\\"
    folder = folder.strip("\\")
    # make exclude_option to string
    exclude_str = ""
    for string in exclude:
        exclude_str += f"-xr!{string} "
    # 7z command line
    os.system(f'7z a -t7z "{location}{date}\\{name}-{date}" "{folder}" -mmt{cores} -mx=1 {exclude_str}')


if __name__ == "__main__":
    folders = parse("files", is_list=True)
    pool = multiprocessing.Pool(len(folders))
    pool.map(prepare, folders)
    pool.close()
    pool.join()
