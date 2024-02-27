from fastapi import APIRouter


router = APIRouter(prefix="/health-checker")


@router.get("/")
def health_checker():
    try:
        return {'message': 'The server is running!'}
    except Exception as e:
        return {'message': f'An error occurred: {e}'}
