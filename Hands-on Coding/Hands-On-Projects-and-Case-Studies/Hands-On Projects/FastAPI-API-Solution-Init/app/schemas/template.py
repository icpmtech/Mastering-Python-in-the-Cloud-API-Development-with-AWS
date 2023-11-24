from pydantic import BaseModel


class AidcTemplateIn(BaseModel):
    name: str
    author: str
    book: str


# class AidcPartitionOutSchema(BaseModel):
#     status: str
#     data: Union[AidcPartitionOut, List[AidcPartitionOut]] | None = None
#     message: str | None = None