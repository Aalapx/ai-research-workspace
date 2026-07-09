from pathlib import Path

class DocumentService:
    def __init__(self):
        self.upload_directory = Path("storage/uploads")

    async def process_document(self, file):
        if not file.filename.endswith(".pdf"):
            return {
                "success": False,
                "message": "Only PDF files are supported",
                "filename": file.filename
            }

        content = await file.read()
        file_path = self.upload_directory / file.filename
        file_path.write_bytes(content)
        
        return {
            "success": True,
            "message": "Document received",
            "filename": file.filename,
            "stored_path": str(file_path)
        }
            
