from main import LetsGoo

data = [
    {
<<<<<<< HEAD
<<<<<<< HEAD
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

count = 0

for datax in data:
    count +=1
    letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'], len(data), count)
    letsgo.letsinput()
    
=======
=======
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
        "ODP": "ODP-BLI-FR/56",
        "SERVICE": "172405800712",
        "PORT": "3"
    }
]


for datax in data:
    letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'])
<<<<<<< HEAD
    letsgo.letsinput()
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
=======
    letsgo.letsinput()
>>>>>>> 52cec794f8945946f2e0b625c3a03dd51c1378dd
