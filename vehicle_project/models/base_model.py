class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    @classmethod
    def get_obj_from_json(cls, json_data):
        """
        :param json_data: json data for creating object
        :return: object ot objects list
        """
        return [cls(**data) for data in json_data] if isinstance(json_data, list) else cls(**json_data)