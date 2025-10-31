from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Optional
from app.schemas.note_schemas import NoteCreateRequest
from app.api.auth import get_user_id
from app.services.supabase_services import supabase

router = APIRouter()

#CREATE NOTE
@router.post("/notes")
def create_note(
    body: NoteCreateRequest,
    user_id: str = Depends(get_user_id)
):
    try:
        data = {
            "user_id": user_id,
            "title": body.title,
            "content": body.content,
            "pinned": body.pinned,
            "favorite": body.favorite,
            "created_at": body.created_at.isoformat(),
            "updated_at": body.updated_at.isoformat(),
        }

        response = supabase.table("notes").insert(data).execute()

        if not response.data:
            raise HTTPException(status_code=400, detail="Note could not be created")

        return {"message": "Note created successfully", "note": response.data[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notes")
def get_notes(user_id: str = Depends(get_user_id)):
    try:
        response = (
            supabase.table("notes")
            .select("*")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )

        if response.data is None:
            return {"notes": []}

        return {"notes": response.data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#UPDATE NOTE
@router.put("/notes/{note_id}")
def update_note(
    note_id: str = Path(..., description="UUID of the note"),
    body: NoteCreateRequest = None,
    user_id: str = Depends(get_user_id)
):
    try:
        data = {
            "title": body.title,
            "content": body.content,
            "pinned": body.pinned,
            "favorite": body.favorite,
            "updated_at": body.updated_at.isoformat(),
        }

        response = (
            supabase.table("notes")
            .update(data)
            .eq("id", note_id)
            .eq("user_id", user_id)
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=404, detail="Note not found or not owned by user")

        return {"message": "Note updated successfully", "note": response.data[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#DELETE NOTE
@router.delete("/notes/{note_id}")
def delete_note(
    note_id: str = Path(..., description="UUID of the note"),
    user_id: str = Depends(get_user_id)
):
    try:
        response = (
            supabase.table("notes")
            .delete()
            .eq("id", note_id)
            .eq("user_id", user_id)
            .execute()
        )

        if not response.data:
            raise HTTPException(status_code=404, detail="Note not found or not owned by user")

        return {"message": "Note deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
