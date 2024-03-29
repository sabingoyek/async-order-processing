# Local modules
from .models import CustomerModel
from ..database import db, BaseRepository

class CustomersRepository(BaseRepository[CustomerModel]):
    def __init__(self):
        super().__init__(db,"customers")