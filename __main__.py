import sys

from vd import Video

if __name__ == "__main__":
    url = sys.argv[1]
    local_path = sys.argv[2]
    Video(url).download(local_path)
