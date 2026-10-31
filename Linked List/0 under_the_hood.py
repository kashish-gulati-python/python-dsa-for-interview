head = {
        "value": 9,
        "next": {
                "value": 29,
                "next": {
                        "value": 2,
                        "next": {
                                "value": 10,
                                "next": None
                                }
                        }
                }
        }

print(head["next"]["next"]["value"])