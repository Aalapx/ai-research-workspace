class DocumentService:
    def process_document(self, file):
        if not file.filename.endswith(".pdf"):
            return {
                "success": False,
                "message": "Only PDF files are supported",
                "filename": file.filename
            }
        
        return {
            "success": True,
            "message": "Document received",
            "filename": file.filename
        }
            
