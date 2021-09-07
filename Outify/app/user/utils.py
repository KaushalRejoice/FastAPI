import json

# to convert the object to string
class ToJson:
    def id_to_str(self, mongo_obj):
        d = {}
        for i in mongo_obj:
            if i == "_id":
                d[i] = str(mongo_obj[i])
            else:
                d[i] = mongo_obj[i]
        return d

    def dict_to_json(self, dict):
        return json.dumps(dict)

    def mongo_to_json(self, mongo_obj, many=False):
        if many:
            d = {}
            i = 0
            for user in mongo_obj:
                i += 1
                user = self.id_to_str(user)
                json_user = self.dict_to_json(user)
                d[i] = json_user
            json_res = json.dumps(d)
            return json_res

        else:   
            return self.dict_to_json(self.id_to_str(mongo_obj))

    