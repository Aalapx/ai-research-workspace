from fastapi import APIRouter, File, UploadFile

from app.services.document_service import DocumentService

router = APIRouter()

@router.post("/documents")
def create_document(file: UploadFile = File(...)):
    document_service = DocumentService()
    result = document_service.process_document(file)

    return result

