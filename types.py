class JsonDeserializable(object):
    """
    Subclasses of this class are guaranteed to be able to be created from a json-style dict or json formatted string.
    All subclasses of this class must override de_json.
    """

    @classmethod
    def de_json(cls, json_type):
        """
        Returns an instance of this class from the given json dict or string.
        This function must be overridden by subclasses.
        :return: an instance of this class created from the given json dict or string.
        """
        raise NotImplementedError

    @staticmethod
    def check_json(json_type):
        """
        Checks whether json_type is a dict or a string. If it is already a dict, it is returned as-is.
        If it is not, it is converted to a dict by means of json.loads(json_type)
        :param json_type:
        :return:
        """
        try:
            str_types = (str, unicode)
        except NameError:
            str_types = (str,)

        if type(json_type) == dict:
            return json_type
        elif type(json_type) in str_types:
            return json.loads(json_type)
        else:
            raise ValueError("json_type should be a json dict or string.")

class Homework(JsonDeserializable):
    def __init__ (self,status,theme,overdueTime,created,spec,specId,teacherFullName,taskFileName,taskFilePath,mustDoneBy,uploadDate,uploadFileName,uploadId,uploadPath):
        self.status = status
        self.theme = theme
        self.overdueTime = overdueTime
        self.created = created
        self.spec = spec
        self.specId = specId
        self.teacherFullName = teacherFullName
        self.taskFileName = taskFileName
        self.taskFilePath = taskFilePath
        self.mustDoneBy = mustDoneBy
        self.homework = {
            'uploadDate':uploadDate,
            'uploadPath':uploadPath,
            'uploadFileName':uploadFileName,
            'uploadId':uploadId
        }
    pass