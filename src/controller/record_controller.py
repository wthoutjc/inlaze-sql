from fastapi import APIRouter, HTTPException
from src.func.handle_record import get_record_count

router = APIRouter()

@router.get("/records/count")
def get_record_count_route():
    try:
        db_config = {
            'host': 'localhost',
            'dbname': 'inlaze-sql',
            'user': 'postgres',
            'password': 'some_password'
        }
        table_name = 'mi_tabla'

        total_records = get_record_count(db_config, table_name)
        return {"count": total_records}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
