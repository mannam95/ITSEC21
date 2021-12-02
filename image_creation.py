import minutiae_map


def create_image(path):
    create_image_from_map(parse(path))


def parse(path):
    m_map = minutiae_map.MinutiaeMap()
    with open(path) as f:
        lines = f.readlines()
        m_map.minutiae_list = [read_minutiae(list(map(int, x.split()))) for x in lines]
    return m_map


def read_minutiae(arr):
    return minutiae_map.MinutiaeInformation(arr[0], arr[1], arr[2])

def create_image_from_map(minutiae_map):
    print('test')
