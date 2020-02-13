from main import LetsGoo

data = [
    {
        "ODP": "ODP-BLI-FR/47",
        "SERVICE": "172405203008",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/48",
        "SERVICE": "36692295",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/48",
        "SERVICE": "172405803521",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/48",
        "SERVICE": "172405803195",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/48",
        "SERVICE": "172405803621",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FN/07",
        "SERVICE": "172405206476",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FN/07",
        "SERVICE": "172405206484",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FN/07",
        "SERVICE": "172405206489",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FN/07",
        "SERVICE": "172405203097",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405800844",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405800405",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405203129",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405203691",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405203183",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405800940",
        "PORT": "7"
    },
    {
        "ODP": "ODP-BLI-FR/14",
        "SERVICE": "172405800503",
        "PORT": "8"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "3665502022",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "3665501838",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "172405802724",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "172405803822",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "172405803694",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "172405800902",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FD/21",
        "SERVICE": "172405803692",
        "PORT": "7"
    },
    {
        "ODP": "ODP-BLI-FAA/01",
        "SERVICE": "172405203595",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FAA/01",
        "SERVICE": "172405220380",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FAA/01",
        "SERVICE": "172405203169",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FAA/01",
        "SERVICE": "172405800483",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FAA/01",
        "SERVICE": "172405203155",
        "PORT": "7"
    },
    {
        "ODP": "ODP-BLI-FR/55",
        "SERVICE": "36691137",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/55",
        "SERVICE": "36693791",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/55",
        "SERVICE": "172405802768",
        "PORT": "7"
    },
    {
        "ODP": "ODP-BLI-FR/45",
        "SERVICE": "172405803531",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/45",
        "SERVICE": "172405803098",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/45",
        "SERVICE": "172405803568",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/45",
        "SERVICE": "172405802767",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/45",
        "SERVICE": "172405803664",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/45",
        "SERVICE": "172405803854",
        "PORT": "8"
    },
    {
        "ODP": "ODP-BLI-FR/62",
        "SERVICE": "172405803278",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/62",
        "SERVICE": "172405802848",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/62",
        "SERVICE": "172405218070",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/62",
        "SERVICE": "172405800915",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/62",
        "SERVICE": "172405802150",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/62",
        "SERVICE": "172405800927",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/61",
        "SERVICE": "172405802871",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/61",
        "SERVICE": "172405800860",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/61",
        "SERVICE": "172405220404",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FAB/06",
        "SERVICE": "172405802234",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FAB/06",
        "SERVICE": "172405802891",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FAB/06",
        "SERVICE": "172405803392",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FAB/06",
        "SERVICE": "172405803406",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FAB/06",
        "SERVICE": "172405802598",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FAB/12",
        "SERVICE": "172405802641",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FAB/12",
        "SERVICE": "172405803015",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FAB/12",
        "SERVICE": "172405803315",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FAB/12",
        "SERVICE": "172405803794",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/01",
        "SERVICE": "172405203690",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/01",
        "SERVICE": "172405203060",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/01",
        "SERVICE": "172405220365",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/01",
        "SERVICE": "172405203236",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/01",
        "SERVICE": "172405206237",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/03",
        "SERVICE": "172405802889",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/03",
        "SERVICE": "172405203241",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/03",
        "SERVICE": "172405800334",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/03",
        "SERVICE": "172405203380",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FE/18",
        "SERVICE": "172428800335",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FE/18",
        "SERVICE": "172428802568",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "172405802906",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "172405800932",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "172405802361",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "172405803462",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "172405802648",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "3665501896",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/42",
        "SERVICE": "172405802867",
        "PORT": "7"
    },
    {
        "ODP": "ODP-BLI-FR/04",
        "SERVICE": "172405206141",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/04",
        "SERVICE": "172405203493",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/04",
        "SERVICE": "172405203110",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/04",
        "SERVICE": "172405800397",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405802537",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405800872",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405800834",
        "PORT": "3"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405800718",
        "PORT": "4"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405803000",
        "PORT": "5"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405802691",
        "PORT": "6"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405203602",
        "PORT": "7"
    },
    {
        "ODP": "ODP-BLI-FR/06",
        "SERVICE": "172405802657",
        "PORT": "8"
    },
    {
        "ODP": "ODP-BLI-FR/56",
        "SERVICE": "172405802710",
        "PORT": "1"
    },
    {
        "ODP": "ODP-BLI-FR/56",
        "SERVICE": "172405803230",
        "PORT": "2"
    },
    {
        "ODP": "ODP-BLI-FR/56",
        "SERVICE": "172405800712",
        "PORT": "3"
    }
]


for datax in data:
    letsgo = LetsGoo(datax['ODP'], datax['SERVICE'], datax['PORT'])
    letsgo.letsinput()