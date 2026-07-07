from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.document_service import DocumentService

router = APIRouter()

@router.post("/documents")
def create_document(file: UploadFile = File(...)):
    document_service = DocumentService()
    result = document_service.process_document(file)

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )


    return result

