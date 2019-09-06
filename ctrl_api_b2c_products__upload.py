import json

from django.http import HttpResponse

from sync.tasks import task_manager


# @class_declaration interna_upload #
class interna_upload():
    pass


# @class_declaration nobuckalma_sync_upload #
class nobuckalma_sync_upload(interna_upload):

    @staticmethod
    def start(pk, data):
        response = task_manager.task_executer("products_upload", data)

        result = response["data"]
        status = response["status"]

        return HttpResponse(json.dumps(result), status=status, content_type="application/json")


# @class_declaration upload #
class upload(nobuckalma_sync_upload):
    pass
