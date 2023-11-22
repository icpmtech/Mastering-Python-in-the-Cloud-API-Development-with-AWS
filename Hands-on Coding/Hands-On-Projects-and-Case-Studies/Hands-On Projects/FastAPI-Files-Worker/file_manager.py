from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  TemplateFiles
from datetime import datetime
import ast
from   manager_csv import manager_csv
import os
async def get_file(file_name:str):
    try:
        file = await TemplateFiles.filter( file_name = file_name).first()
                                      
    except DoesNotExist as e:
        raise HTTPException(status_code=404, detail=f"File template name not found.{e}")
    converted_content_file_to_dict = ast.literal_eval(file.file_content)
    try:
     file_output = manager_csv.generate_csv(converted_content_file_to_dict,file.file_name)
    except OSError as os_error :
        raise HTTPException(status_code=404, detail=f"Error processing file .{os_error}")
    return file_output
async def delete_file(file_name:str):

    file_path="generated_templates\\" + file_name + ".csv"
    try:
     if os.path.exists("generated_templates"):
        os.remove(file_path)
    except OSError as os_error :
        raise HTTPException(status_code=404, detail=f"Error in processing file on delete operation.{os_error}")
    return f"File: {file_name}.csv was removed."

async def create_file_template(content, filename):
     
    file_id_timestap_flag = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        file = await TemplateFiles.create( file_id_timestap = file_id_timestap_flag, file_name = filename,file_content = content)
                                        
    except IntegrityError:
        raise HTTPException(status_code=401, detail=f"File template name already exists.")

    return file