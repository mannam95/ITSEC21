import itertools
from collections import defaultdict
import re
from read_files import read_files


def read_files_split_into_groups(dir_path):
    """This function separates into groups by second underscore. 

    :param dir_path: the fingerprints directory path.
    :return: Returns all groups.
    """
    
    groups = defaultdict(list)
    files = read_files(dir_path)

    groups =  [list(g) for _, g in itertools.groupby(sorted(files), lambda x: x[0:[m.start() for m in re.finditer(r"_",x)][1]])]

    return groups