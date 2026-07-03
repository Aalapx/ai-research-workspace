class DocumentService:
    def process_document(self, file):
        result = {
            "message": "Document received",
            "filename": file.filename
        }
        return result
        