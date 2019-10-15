from import_export import resources

from .models import Student,RollnoRegnoMap

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class AttendenceResource(resources.ModelResource):
    class Meta:
        model = RollnoRegnoMap
        exclude =('time','ftotal','id',)
        ordering = ('time')