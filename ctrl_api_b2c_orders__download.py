import json

from django.http import HttpResponse

from sync.tasks import task_manager


# @class_declaration interna_download #
class interna_download():
    pass


# @class_declaration nobuckalma_sync_download #
class nobuckalma_sync_download(interna_download):

    @staticmethod
    def start(pk, data):
        response = task_manager.task_executer("orders_download", data)

        result = response["data"]
        status = response["status"]

        return HttpResponse(json.dumps(result), status=status, content_type="application/json")


# @class_declaration download #
class download(nobuckalma_sync_download):
    pass
