import json
from bson.json_util import dumps


# to convert the dict_object/mongo_obj to string
class ToJson:
    # Converts ObjectId to string
    def id_to_str(self, mongo_obj):
        d = {k: v if k != '_id' else str(v) for k, v in mongo_obj.items()}
        return d

    # Converts dictio
    def dict_to_json(self, dict):
        return json.dumps(dict)

    def mongo_to_json_kv(self, mongo_obj, many=False):
        """
        returns json as key and value pair
        """
        if many:
            d = {k: self.dict_to_json(
                self.id_to_str(user)) for k, user in zip(range(many), mongo_obj)}
        else:
            d = {0: self.dict_to_json(self.id_to_str(mongo_obj))}

        json_res = json.dumps(d)
        return json_res

    def mongo_to_json(self, obj):
        "Returns json as list"
        r1 = dumps(obj)
        return r1


def to_dict(obj):
    return {k: v if k != '_id' else str(v) for k, v in obj.items()}

def to_list_of_dict(objs):
    return [to_dict(obj) for obj in objs]
    