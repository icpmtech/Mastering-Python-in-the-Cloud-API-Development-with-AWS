import logging

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from tortoise.transactions import in_transaction

import app.api.templates.book.managers.aidc_internet_telepac_template as ManagerGenerateTemplate
import app.api.templates.book.managers.files.file_manager as ManagerFile
import app.api.templates.book.managers.aidc_internet_telepac_template1 as ManagerGenerateTemplate1
from app.schemas.book import AidcTemplateIn
from starlette.responses import FileResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/book/file")
async def get_file(file_name:str):
    file_path=await ManagerFile.get_file(file_name)
    return FileResponse(file_path, media_type='application/octet-stream',filename=file_path)

@router.delete("/book/file")
async def delete_file(file_name:str):
    try:
        file_message=await ManagerFile.delete_file(file_name)
        return {
                "status": "success",
                "data": file_message
                }
    except HTTPException as exc:
        return JSONResponse(content={
                "status": "fail",
                "message": exc.detail
            }, status_code=exc.status_code)
    except Exception as exc:
            logger.error(exc.args, exc_info=True)
            return JSONResponse(content={
                "status": "error",
                "error": "Internal Server Error"
            }, status_code=500)
    return file_message

@router.post("/api/v1/book", description="create config template book")
async def create_config_template_telepac(input: AidcTemplateIn):
    ##async with in_transaction():
        try:
            template = await ManagerGenerateTemplate.generate_template(input)
            return {
                "status": "success",
                "data": template
                }
        except HTTPException as exc:
            return JSONResponse(content={
                "status": "fail",
                "message": exc.detail
            }, status_code=exc.status_code)
        except Exception as exc:
            logger.error(exc.args, exc_info=True)
            return JSONResponse(content={
                "status": "error",
                "error": "Internal Server Error"
            }, status_code=500)
        

    ##async with in_transaction():
        try:
            template = await ManagerGenerateTemplate1.generate_template(input)
            return {
                "status": "success",
                "data": template
                }
        except HTTPException as exc:
            return JSONResponse(content={
                "status": "fail",
                "message": exc.detail
            }, status_code=exc.status_code)
        except Exception as exc:
            logger.error(exc.args, exc_info=True)
            return JSONResponse(content={
                "status": "error",
                "error": "Internal Server Error"
            }, status_code=500)