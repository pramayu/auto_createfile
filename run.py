from tqdm import tqdm
from main import LetsGoo

data = [
    {
        "ODP": "ODP-BLI-FF/04",
        "SERVICE": "172405800777",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/69",
        "SERVICE": "172405803097",
        "PORT": "2"
    },
]

loop = tqdm(total = len(data), position=0, disable=False)

for datax in data:
    letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'])
    letsgo.letsinput()
    loop.set_description("Loading...".format(datax))
    loop.update(1)
loop.close()