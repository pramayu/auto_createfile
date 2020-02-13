from main import LetsGoo

data = [
    {
        "ODP": "ODP-BLI-FR/56",
        "SERVICE": "172405800712",
        "PORT": "3"
    }
]


for datax in data:
    letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'])
    letsgo.letsinput()