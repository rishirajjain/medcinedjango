from django_elasticsearch_dsl import DocType, Index
from medicines.models import BoerickConv

medic = Index('medic')

@medic.doc_type
class PostDocument(DocType):
    class Meta:
        model = BoerickConv

        fields = [
            'book_name',
            'med_name',
            'section',
            'med_details',
        ]