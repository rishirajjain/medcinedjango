from django_elasticsearch_dsl import DocType, Index
from medicines.models import Medicines

medicine = Index('medicine')

@medicine.doc_type
class PostDocument(DocType):
    class Meta:
        model = Medicines

        fields = [
            'bookName',
            'medName',
            'medDetails',
        ]