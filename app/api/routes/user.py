from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_schemas import UpdateNameRequest
from app.api.auth import get_user_id
from app.services.supabase_services import supabase

router = APIRouter()

@router.put("/fullname")
def update_fullname(
    body: UpdateNameRequest,
    user_id: str = Depends(get_user_id)
):
    try:
        response = supabase.table("profiles") \
            .update({"full_name": body.full_name}) \
            .eq("id", user_id) \
            .execute()

        if len(response.data) == 0:
            raise HTTPException(status_code=404, detail="Profile not found")

        return {"message": "Full name updated successfully", "data": response.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/profile")
def get_profile(user_id: str = Depends(get_user_id)):
    try:
        response = supabase.table("profiles") \
            .select("id, full_name, created_at") \
            .eq("id", user_id) \
            .single() \
            .execute()

        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")

        return response.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))