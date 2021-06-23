from lxml import etree
from beamparse.inputs.factory import TemplateLoader


data = {
    "population": [
        {
            "attributes": [
                {"name": "age", "type": "java.lang.Integer", "value": 28},
                {"name": "sex", "type": "java.lang.String", "value": "M"},
            ],
            "plan": [
                {
                    "type": "Home",
                    "y": "4524819.50223867",
                    "x": "408202.0350928387",
                    "end_time": "9:00:00",
                },
                {
                    "type": "School",
                    "y": "4525378.715445407",
                    "x": "409050.5632430612",
                    "end_time": "17:00:00",
                    "mode": "walk",
                },
                {
                    "type": "Home",
                    "y": "4524819.50223867",
                    "x": "408202.0350928387",
                    "mode": "walk",
                },
            ],
        },
        {
            "attributes": [
                {"name": "age", "type": "java.lang.Integer", "value": 25},
                {"name": "sex", "type": "java.lang.String", "value": "F"},
            ],
            "plan": [
                {
                    "type": "Home",
                    "y": "4524819.50223867",
                    "x": "408202.0350928387",
                    "end_time": "9:00:00",
                },
                {
                    "type": "Other",
                    "y": "4524671.101160721",
                    "x": "408411.3689155844",
                    "end_time": "12:00:00",
                    "mode": "walk",
                },
                {
                    "type": "Home",
                    "y": "4524819.50223867",
                    "x": "408202.0350928387",
                    "mode": "walk",
                },
            ],
        },
    ]
}


def test_render():
    """
    Test that the resultant XML file is structured like the input data.
    """
    output = TemplateLoader("population", data).render()
    tree = etree.fromstring(output.encode("utf-8"))
    assert len(tree.xpath("//person")) == len(data["population"])
    for i, pop in enumerate(data["population"], 1):
        assert len(tree.xpath(f"//person[{i}]/plan/activity")) == len(pop["plan"])
        assert len(tree.xpath(f"//person[{i}]/attributes/attribute")) == len(
            pop["attributes"]
        )
