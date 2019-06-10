from django_elasticsearch_dsl import DocType, Index
from medicines.models import BoerickeJoints

medic = Index('medic')

@medic.doc_type
class PostDocument(DocType):
    class Meta:
        model = BoerickeJoints

        fields = [
            'medicine',
            'section',
            'details',
        ]